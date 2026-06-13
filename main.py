from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.api.stream import router as stream_router

app = FastAPI(
    title="Multi-Agent Research Assistant"
)

# Added explicit Vercel URLs to prevent FastAPI startup crashes
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://multi-agent-research-assistant-rho.vercel.app", # Your main production URL
        "https://multi-agent-research-assistant-pfdlmzwg0.vercel.app", # The specific preview URL from your console error
        "http://localhost:5173", # For local testing
    ],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(router)

app.include_router(
    stream_router
)