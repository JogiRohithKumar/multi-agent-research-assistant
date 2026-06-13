import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import QueryBox from './components/QueryBox';
import AgentPanel from './components/AgentPanel';
import ReportPanel from './components/ReportPanel';
import PapersPanel from './components/PapersPanel';

const BACKEND_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
const API_KEY = 'research-assistant-demo-key';

export default function App() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Initialize state from sessionStorage so data survives a page refresh or "Back" button
  const [events, setEvents] = useState(() => JSON.parse(sessionStorage.getItem('savedEvents')) || []);
  const [report, setReport] = useState(() => JSON.parse(sessionStorage.getItem('savedReport')) || null);
  const [papers, setPapers] = useState(() => JSON.parse(sessionStorage.getItem('savedPapers')) || []);

  const handleSearch = async (query) => {
    setLoading(true);
    setEvents([]);
    setReport(null);
    setPapers([]);
    setError(null);

    // Clear old storage when a new search starts
    sessionStorage.removeItem('savedEvents');
    sessionStorage.removeItem('savedReport');
    sessionStorage.removeItem('savedPapers');

    // 1. Start polling the /stream endpoint for timeline updates
    const pollInterval = setInterval(async () => {
      try {
        const streamRes = await fetch(`${BACKEND_URL}/stream`, {
            method: 'GET',
            headers: { 'accept': 'application/json' }
        });
        if (streamRes.ok) {
          const streamData = await streamRes.json();
          if (streamData.events) {
            setEvents(streamData.events);
            // Save events as they stream in
            sessionStorage.setItem('savedEvents', JSON.stringify(streamData.events));
          }
        }
      } catch (e) {
        console.warn("Polling stream failed", e);
      }
    }, 1000);

    // 2. Fetch the actual research data
    try {
      const response = await fetch(`${BACKEND_URL}/research`, {
        method: 'POST',
        headers: {
          'accept': 'application/json',
          'Content-Type': 'application/json',
          'x-api-key': API_KEY
        },
        body: JSON.stringify({ query }),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();

      // Extract the first paper's summary to act as the Executive Summary
      const mainSummary = data.summaries && data.summaries.length > 0 
        ? data.summaries[0].summary 
        : "Intelligence data synthesized successfully.";

      const finalReport = {
        summary: mainSummary,
        findings: data.intelligence?.verification?.common_findings || [],
        gaps: data.intelligence?.gaps?.research_gaps || [],
        future: data.intelligence?.gaps?.future_directions || []
      };

      setReport(finalReport);
      // Save report to session storage
      sessionStorage.setItem('savedReport', JSON.stringify(finalReport));

      // Map the papers array and format authors/dates nicely
      const formattedPapers = (data.papers || []).map((paper, index) => {
        let authorString = "Unknown";
        if (Array.isArray(paper.authors)) {
          authorString = paper.authors.slice(0, 2).join(', ') + (paper.authors.length > 2 ? ' et al.' : '');
        }
        const year = paper.published ? new Date(paper.published).getFullYear().toString() : "N/A";

        return {
          id: index,
          title: paper.title,
          authors: authorString,
          published: year,
          link: paper.paper_url
        };
      });

      setPapers(formattedPapers);
      // Save papers to session storage
      sessionStorage.setItem('savedPapers', JSON.stringify(formattedPapers));

    } catch (err) {
      console.error("Failed to generate research:", err);
      setError("An error occurred while fetching the research data. Ensure your backend is running.");
    } finally {
      // 4. Cleanup
      clearInterval(pollInterval);
      setLoading(false);
      
      // Do one final fetch to ensure we got the very last events after loading finishes
      try {
        const finalStreamRes = await fetch(`${BACKEND_URL}/stream`);
        const finalStreamData = await finalStreamRes.json();
        if (finalStreamData.events) {
          setEvents(finalStreamData.events);
          sessionStorage.setItem('savedEvents', JSON.stringify(finalStreamData.events));
        }
      } catch(e) {}
    }
  };

  return (
    <div className="min-h-screen bg-[#09090b] bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.15),rgba(255,255,255,0))] text-slate-200 p-4 md:p-8 font-sans selection:bg-indigo-500/30">
      <div className="max-w-[1400px] mx-auto space-y-6">
        <Header />
        
        <QueryBox onSearch={handleSearch} loading={loading} />
        
        {error && (
          <div className="bg-red-500/10 border border-red-500/20 text-red-400 px-4 py-3 rounded-xl text-sm font-medium">
            {error}
          </div>
        )}
        
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div className="lg:col-span-3 sticky top-6">
            <AgentPanel events={events} loading={loading} />
          </div>

          <div className="lg:col-span-6">
            <ReportPanel report={report} loading={loading} />
          </div>

          <div className="lg:col-span-3 sticky top-6">
            <PapersPanel papers={papers} loading={loading} />
          </div>
        </div>
      </div>
    </div>
  );
}