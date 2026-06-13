from typing import TypedDict, Annotated
import operator

from langgraph.graph import StateGraph, START, END

from app.db.checkpoint import checkpointer
from app.memory.memory_manager import save_session

from app.agents.search_agent import search_papers
from app.agents.summary_agent import summarize_papers
from app.agents.citation_agent import generate_citations
from app.agents.research_intelligence_agent import generate_research_intelligence
from app.agents.report_agent import generate_report
from app.agents.supervisor_agent import generate_supervisor_decision

from app.utils.safe_execute import safe_execute
from app.utils.stream_logger import stream_log, clear_stream_events

from app.rag.vector_store import store_papers


# -----------------------------
# STATE
# -----------------------------

class ResearchState(TypedDict):
    thread_id: str
    query: str

    supervisor: dict

    papers: list
    summaries: list
    citations: list

    intelligence: dict
    report: str

    agent_logs: Annotated[list, operator.add]


# -----------------------------
# SUPERVISOR
# -----------------------------

def supervisor_node(state: ResearchState):

    result = safe_execute(
        "Supervisor Agent",
        generate_supervisor_decision,
        state["query"]
    )

    if not result["success"]:
        return {
            "supervisor": {
                "status": "valid",
                "route": "continue"
            }
        }

    return {
        "supervisor": result["result"]
    }


def supervisor_router(state):

    decision = state.get("supervisor", {})

    if decision.get("status") == "invalid":
        return END

    return "search"


# -----------------------------
# SEARCH
# -----------------------------

def search_node(state: ResearchState):

    clear_stream_events()

    result = safe_execute(
        "Search Agent",
        search_papers,
        state["query"]
    )

    if not result["success"]:
        return {
            "agent_logs": [{
                "agent": "search",
                "status": "failed",
                "error": result["error"]
            }]
        }

    stream_log("Search Agent Completed")

    return {
        "papers": result["result"],
        "agent_logs": [{
            "agent": "search",
            "status": "success"
        }]
    }


def search_router(state):

    if len(state.get("papers", [])) == 0:
        return END

    return "summary"


# -----------------------------
# SUMMARY
# -----------------------------

def summary_node(state: ResearchState):

    result = safe_execute(
        "Summary Agent",
        summarize_papers,
        state["papers"]
    )

    if not result["success"]:
        return {
            "agent_logs": [{
                "agent": "summary",
                "status": "failed",
                "error": result["error"]
            }]
        }

    stream_log("Summary Agent Completed")

    return {
        "summaries": result["result"],
        "agent_logs": [{
            "agent": "summary",
            "status": "success"
        }]
    }


def summary_router(state):

    if not state.get("summaries"):
        return END

    return "citation"


# -----------------------------
# CITATION
# -----------------------------

def citation_node(state: ResearchState):

    result = safe_execute(
        "Citation Agent",
        generate_citations,
        state["papers"]
    )

    if not result["success"]:
        return {
            "agent_logs": [{
                "agent": "citation",
                "status": "failed",
                "error": result["error"]
            }]
        }

    stream_log("Citation Agent Completed")

    return {
        "citations": result["result"],
        "agent_logs": [{
            "agent": "citation",
            "status": "success"
        }]
    }


# -----------------------------
# INTELLIGENCE
# -----------------------------

def intelligence_node(state: ResearchState):

    result = safe_execute(
        "Research Intelligence Agent",
        generate_research_intelligence,
        state["query"],
        state["summaries"],
        state["citations"]
    )

    if not result["success"]:
        return {
            "agent_logs": [{
                "agent": "intelligence",
                "status": "failed",
                "error": result["error"]
            }]
        }

    intelligence = result["result"]

    stream_log("Research Intelligence Completed")

    return {
        "intelligence": intelligence,
        "report": intelligence.get("report", ""),
        "agent_logs": [{
            "agent": "intelligence",
            "status": "success"
        }]
    }


# -----------------------------
# REPORT
# -----------------------------

def report_node(state: ResearchState):

    report = generate_report(
        state["query"],
        state["summaries"],
        state["citations"],
        intelligence = state.get("intelligence", {})
    )

    save_session(
        state["query"],
        {
            "query": state["query"],
            "papers": state["papers"],
            "summaries": state["summaries"],
            "citations": state["citations"],
            "intelligence": state["intelligence"],
            "report": report
        }
    )

    stream_log("Report Generated")

    return {
        "report": report
    }


# -----------------------------
# RAG
# -----------------------------

def rag_node(state: ResearchState):

    store_papers(state["papers"])

    return {}


# =====================================================
# GRAPH
# =====================================================

builder = StateGraph(ResearchState)

builder.add_node("supervisor", supervisor_node)
builder.add_node("search", search_node)
builder.add_node("summary", summary_node)
builder.add_node("citation", citation_node)
builder.add_node("rag", rag_node)
builder.add_node("intelligence", intelligence_node)
builder.add_node("report", report_node) 


# ENTRY
builder.add_edge(START, "supervisor")


# FLOW
builder.add_conditional_edges("supervisor", supervisor_router)

builder.add_edge("search", "rag")
builder.add_edge("rag", "summary")

builder.add_conditional_edges("summary", summary_router)

builder.add_edge("citation", "intelligence")
builder.add_edge("intelligence", "report")

builder.add_edge("report", END)


research_graph = builder.compile(
    checkpointer=checkpointer
)