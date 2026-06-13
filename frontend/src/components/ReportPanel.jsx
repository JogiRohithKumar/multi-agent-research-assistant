import React from 'react';
import { FileText, ChevronRight } from 'lucide-react';

export default function ReportPanel({ report, loading }) {
  if (!report && !loading) {
    return (
      <div className="h-[600px] flex flex-col items-center justify-center bg-[#11131a]/80 backdrop-blur-xl border border-white/5 rounded-2xl p-8 shadow-2xl text-center">
        <div className="w-16 h-16 bg-white/5 rounded-2xl flex items-center justify-center mb-4">
          <FileText className="w-8 h-8 text-slate-600" />
        </div>
        <h3 className="text-lg font-medium text-slate-300 mb-1">No Report Generated</h3>
        <p className="text-slate-500 text-sm max-w-sm">Enter a query above to dispatch the agent network. Your synthesized intelligence brief will appear here.</p>
      </div>
    );
  }

  if (!report && loading) {
    return (
      <div className="h-[600px] bg-[#11131a]/80 backdrop-blur-xl border border-white/5 rounded-2xl p-8 shadow-2xl overflow-hidden relative">
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-[#11131a]/50 to-[#11131a] z-10" />
        <div className="animate-pulse space-y-8 opacity-20">
          <div className="h-8 bg-white/20 rounded w-1/3"></div>
          <div className="space-y-3"><div className="h-4 bg-white/20 rounded w-full"></div><div className="h-4 bg-white/20 rounded w-5/6"></div></div>
          <div className="space-y-3"><div className="h-4 bg-white/20 rounded w-full"></div><div className="h-4 bg-white/20 rounded w-4/6"></div></div>
        </div>
      </div>
    );
  }

  return (
    <div className="h-full min-h-[600px] bg-[#11131a]/80 backdrop-blur-xl border border-white/5 rounded-2xl p-8 shadow-2xl">
      <div className="flex items-center gap-3 mb-8 pb-4 border-b border-white/5">
        <FileText className="w-6 h-6 text-indigo-400" />
        <h2 className="text-xl font-bold text-slate-100 tracking-tight">Intelligence Brief</h2>
      </div>
      
      <div className="space-y-8">
        <section>
          <h3 className="text-sm font-bold uppercase tracking-wider text-indigo-400 mb-3 flex items-center gap-2">
            <ChevronRight className="w-4 h-4" /> Executive Summary
          </h3>
          <p className="text-slate-300 leading-relaxed bg-white/5 rounded-xl p-5 border border-white/5">
            {report.summary}
          </p>
        </section>

        <section>
          <h3 className="text-sm font-bold uppercase tracking-wider text-emerald-400 mb-3 flex items-center gap-2">
            <ChevronRight className="w-4 h-4" /> Key Findings
          </h3>
          <ul className="grid gap-2">
            {report.findings.map((item, i) => (
              <li key={i} className="flex items-start gap-3 text-slate-300 bg-white/[0.02] p-3 rounded-lg">
                <span className="mt-1.5 w-1.5 h-1.5 rounded-full bg-emerald-500 shrink-0"></span>
                <span className="leading-relaxed text-sm">{item}</span>
              </li>
            ))}
          </ul>
        </section>

        <section>
          <h3 className="text-sm font-bold uppercase tracking-wider text-amber-400 mb-3 flex items-center gap-2">
            <ChevronRight className="w-4 h-4" /> Research Gaps
          </h3>
          <ul className="grid gap-2">
            {report.gaps.map((item, i) => (
              <li key={i} className="flex items-start gap-3 text-slate-300 bg-white/[0.02] p-3 rounded-lg">
                <span className="mt-1.5 w-1.5 h-1.5 rounded-full bg-amber-500 shrink-0"></span>
                <span className="leading-relaxed text-sm">{item}</span>
              </li>
            ))}
          </ul>
        </section>

        <section>
          <h3 className="text-sm font-bold uppercase tracking-wider text-violet-400 mb-3 flex items-center gap-2">
            <ChevronRight className="w-4 h-4" /> Future Directions
          </h3>
          <ul className="grid gap-2">
            {report.future.map((item, i) => (
              <li key={i} className="flex items-start gap-3 text-slate-300 bg-white/[0.02] p-3 rounded-lg">
                <span className="mt-1.5 w-1.5 h-1.5 rounded-full bg-violet-500 shrink-0"></span>
                <span className="leading-relaxed text-sm">{item}</span>
              </li>
            ))}
          </ul>
        </section>
      </div>
    </div>
  );
}