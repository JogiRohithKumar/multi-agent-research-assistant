from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.api.stream import router as stream_router

app = FastAPI(title="Multi-Agent Research Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://multi-agent-research-assistant-rho.vercel.app",
        "http://localhost:5173",
    ],
    allow_origin_regex=r"https://multi-agent-research-assistant-.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(router)
app.include_router(stream_router)