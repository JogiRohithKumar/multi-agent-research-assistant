import React from 'react';
import { BrainCircuit } from 'lucide-react';

export default function Header() {
  return (
    <header className="w-full flex items-center justify-between bg-[#11131a]/80 backdrop-blur-xl border border-white/5 rounded-2xl p-6 shadow-2xl">
      <div className="flex items-center gap-4">
        <div className="p-3 bg-indigo-500/10 rounded-xl border border-indigo-500/20">
          <BrainCircuit className="w-8 h-8 text-indigo-400" />
        </div>
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-white flex items-center gap-2">
            Research Intelligence
            <span className="px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 text-xs font-semibold border border-indigo-500/20">
              BETA
            </span>
          </h1>
          <p className="text-slate-400 text-sm mt-0.5">Multi-Agent Research Platform</p>
        </div>
      </div>
    </header>
  );
}