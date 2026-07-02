from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from docx_ai_risk_api.routes.analyze import router as analyze_router
from docx_ai_risk_api.routes.health import router as health_router

app = FastAPI(
    title="DOCX AI Risk Analyzer API",
    version="0.1.0",
    description=(
        "Local backend for analyzing DOCX academic documents "
        "for editorial AI-risk markers."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api/v1", tags=["health"])
app.include_router(analyze_router, prefix="/api/v1", tags=["analysis"])
