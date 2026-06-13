import React from 'react';
import { BookOpen, ExternalLink, Library } from 'lucide-react';

export default function PapersPanel({ papers, loading }) {
  return (
    <div className="h-full bg-[#11131a]/80 backdrop-blur-xl border border-white/5 rounded-2xl p-6 shadow-2xl">
      <div className="flex items-center justify-between mb-6 pb-4 border-b border-white/5">
        <div className="flex items-center gap-3">
          <Library className="w-5 h-5 text-indigo-400" />
          <h2 className="text-base font-semibold text-slate-200">Sources</h2>
        </div>
        {papers.length > 0 && (
          <span className="text-xs font-medium text-slate-400 bg-white/5 px-2 py-1 rounded-md">
            {papers.length} Results
          </span>
        )}
      </div>
      
      <div className="space-y-3">
        {papers.length === 0 && !loading ? (
          <div className="text-center py-8 text-slate-500 flex flex-col items-center gap-2">
            <BookOpen className="w-8 h-8 opacity-20" />
            <p className="text-sm">No literature retrieved.</p>
          </div>
        ) : (
          papers.map((paper) => (
            <a 
              key={paper.id} 
              href={paper.link}
              target="_blank" 
              rel="noopener noreferrer"
              className="block bg-[#0a0a0c] border border-white/5 hover:border-indigo-500/50 hover:bg-indigo-500/5 transition-all duration-200 rounded-xl p-4 group"
            >
              <h3 className="text-sm font-medium text-slate-200 leading-snug group-hover:text-indigo-300 transition-colors mb-2">
                {paper.title}
              </h3>
              <div className="flex justify-between items-center text-xs text-slate-400">
                <span className="truncate pr-2">{paper.authors}</span>
                <span className="bg-white/5 px-2 py-0.5 rounded text-slate-300 shrink-0">{paper.published}</span>
              </div>
              <div className="mt-3 flex items-center gap-1.5 text-xs font-medium text-indigo-400 opacity-0 group-hover:opacity-100 transition-opacity">
                <ExternalLink className="w-3 h-3" /> View Source
              </div>
            </a>
          ))
        )}
      </div>
    </div>
  );
}