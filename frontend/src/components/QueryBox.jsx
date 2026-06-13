import React, { useState } from 'react';
import { Search, Sparkles, Loader2 } from 'lucide-react';

export default function QueryBox({ onSearch, loading }) {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim() && !loading) {
      onSearch(query);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="w-full bg-[#11131a]/80 backdrop-blur-xl border border-white/5 rounded-2xl p-3 shadow-2xl flex flex-col md:flex-row gap-3 relative z-10">
      <div className="relative flex-1 flex items-center">
        <Search className="absolute left-4 w-5 h-5 text-slate-500" />
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask anything (e.g., 'Latest trends in Multi-Agent LLMs')..."
          disabled={loading}
          className="w-full bg-[#0a0a0c] border border-white/5 rounded-xl pl-12 pr-4 py-4 text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 focus:border-transparent transition-all disabled:opacity-50"
        />
        <div className="absolute right-4 hidden md:flex items-center gap-1">
          <kbd className="bg-white/5 border border-white/10 rounded px-2 py-1 text-xs text-slate-500 font-mono">↵ Enter</kbd>
        </div>
      </div>
      <button
        type="submit"
        disabled={loading || !query.trim()}
        className="group relative flex items-center justify-center gap-2 bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-500 hover:to-violet-500 text-white px-8 py-4 rounded-xl font-medium transition-all shadow-lg shadow-indigo-900/20 disabled:opacity-50 disabled:cursor-not-allowed overflow-hidden"
      >
        {loading ? (
          <>
            <Loader2 className="w-5 h-5 animate-spin" />
            <span>Researching</span>
          </>
        ) : (
          <>
            <Sparkles className="w-5 h-5" />
            <span>Generate Brief</span>
          </>
        )}
      </button>
    </form>
  );
}