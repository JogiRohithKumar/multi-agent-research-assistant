This `README.md` is designed to highlight your engineering maturity, the complexity of your multi-agent architecture, and your ability to ship production-ready SaaS products.

Copy the content below into your repository’s `README.md` file.

---

# Research Intelligence Assistant 🧠

Research Intelligence Assistant is a production-grade, multi-agent AI research platform designed to automate the end-to-end academic research process. By utilizing a **LangGraph-orchestrated workflow**, the platform goes beyond simple RAG (Retrieval-Augmented Generation) by employing specialized agents to search, verify, summarize, and synthesize complex research data into actionable intelligence briefs.

---

## 🚀 Architecture Overview

The platform leverages a modular, agent-based architecture where every stage of the research pipeline is managed by an autonomous node.

```text
[Frontend: React/Vite] ↔ [Backend: FastAPI] ↔ [LangGraph Orchestration]
                                                       │
         ┌──────────────────┬──────────────────────────┴───────────────┐
         ▼                  ▼                                          ▼
   [Search Agent]    [Summary Agent]   [Citation Agent]   [Intelligence Agent]
         │                  │                  │                       │
         └──────────────────┼──────────────────┼───────────────────────┘
                            ▼
                      [Report Agent] ──▶ [Final Research Brief]

```

---

## 🛠 Technology Stack

* **Orchestration:** LangGraph, LangChain
* **Intelligence:** Google Gemini 2.5 Flash
* **Backend:** Python, FastAPI
* **Frontend:** React, Vite, Tailwind CSS, Axios
* **Database:** ChromaDB (Vector Store), SQLite (Workflow Checkpointing)
* **Deployment:** Vercel (Frontend), Render (Backend)

---

## 🤖 Multi-Agent Workflow

The platform utilizes specialized agents to ensure high-fidelity research:

1. **Supervisor Agent:** Validates query intent and determines the research route.
2. **Query Rewriter:** Expands vague queries into multi-faceted search strings for higher retrieval relevance.
3. **Search Agent:** Executes arXiv-integrated searches and filters for high-relevance academic papers.
4. **Summary Agent:** Extracts executive summaries and key technical findings from raw paper abstracts.
5. **Citation Agent:** Standardizes source attribution into APA format.
6. **Research Intelligence Agent:** Performs cross-paper reasoning to identify **evidence strength**, **common/conflicting findings**, and **research gaps**.
7. **Report Agent:** Synthesizes all agent outputs into a comprehensive, structured research report.

---

## 🌟 Key Engineering Highlights

* **Resilient Agentic Workflow:** Implemented `safe_execute()` and `retry_execute()` patterns to harden the LangGraph against node failures.
* **Production-Ready Security:** Configured secure cross-domain communication between Vercel and Render using Regex-validated CORS middleware.
* **Stateful Orchestration:** Utilized SQLite-based checkpointing to ensure research sessions are persistent and recoverable.
* **Real-time Interaction:** Built a streaming API architecture that provides live visualization of the Agent Network progress in the UI.

---

## 🗺 Roadmap

* [ ] **V2:** User Authentication, persistent Research History, and project workspaces.
* [ ] **V3:** Integration of Semantic Scholar, PubMed, and OpenAlex for multi-source breadth.
* [ ] **V4:** Collaborative research features for team-based workspaces and export capabilities (PDF/DOCX).

---

## 📈 Portfolio Maturity

* **Engineering:** 8.5/10
* **Research Capability:** 8.0/10
* **SaaS Readiness:** 6.0/10

---

## 💡 Get Started

*To run this project locally, clone the repository and configure your environment variables for Gemini API and ChromaDB.*

```bash
# Backend setup
pip install -r requirements.txt
uvicorn main:app --reload

```

*This project represents an end-to-end implementation of an autonomous agent network capable of replacing hours of manual research with seconds of intelligent synthesis.*
