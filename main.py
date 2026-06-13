from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.api.stream import router as stream_router

app = FastAPI(
    title="Multi-Agent Research Assistant"
)

# 2. Add the CORS configuration right here
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://multi-agent-research-assistant-rho.vercel.app", # Your main Vercel production site
        "http://localhost:5173", # Your local laptop testing site
        "*" # This wildcard allows all Vercel preview links to connect safely
    ],
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods including POST and GET
    allow_headers=["*"], # Critical: Allows your custom 'x-api-key' header
)

app.include_router(router)

app.include_router(
    stream_router
)