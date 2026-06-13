import React from 'react';
import { Activity, CheckCircle2, Loader2, CircleDashed } from 'lucide-react';

export default function AgentPanel({ events, loading }) {
  const totalExpectedEvents = 5; 

  return (
    <div className="h-full bg-[#11131a]/80 backdrop-blur-xl border border-white/5 rounded-2xl p-6 shadow-2xl">
      <div className="flex items-center gap-3 mb-6 pb-4 border-b border-white/5">
        <Activity className="w-5 h-5 text-indigo-400" />
        <h2 className="text-base font-semibold text-slate-200">Agent Network</h2>
      </div>
      
      <div className="space-y-6">
        {events.length === 0 && !loading ? (
          <div className="text-center py-8 text-slate-500 flex flex-col items-center gap-2">
            <CircleDashed className="w-8 h-8 opacity-20" />
            <p className="text-sm">Network idle. Awaiting task.</p>
          </div>
        ) : (
          <div className="relative border-l border-white/10 ml-3 space-y-6">
            {events.map((event, index) => (
              <div key={index} className="relative flex items-center gap-4 pl-6">
                <span className="absolute -left-3 flex items-center justify-center w-6 h-6 rounded-full bg-[#11131a] ring-4 ring-[#11131a]">
                  <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                </span>
                <span className="text-sm text-slate-300 font-medium">{event}</span>
              </div>
            ))}
            
            {loading && events.length < totalExpectedEvents && (
              <div className="relative flex items-center gap-4 pl-6">
                <span className="absolute -left-3 flex items-center justify-center w-6 h-6 rounded-full bg-[#11131a] ring-4 ring-[#11131a]">
                  <Loader2 className="w-5 h-5 text-indigo-400 animate-spin" />
                </span>
                <span className="text-sm text-indigo-400 font-medium animate-pulse">Processing next step...</span>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}