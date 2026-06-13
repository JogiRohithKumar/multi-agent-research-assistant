from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.api.stream import router as stream_router

app = FastAPI(title="Multi-Agent Research Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow everything for testing
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(router)
app.include_router(stream_router)