from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from app.api.routes import domain, application
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
#from app.events.consumers import domain_events, application_events

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Admin Service API for ZCare Platform",
    version="0.1.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(domain.router, prefix=settings.API_V1_STR)
app.include_router(application.router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Welcome to ZCare Admin Service"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Event consumers startup and shutdown
"""
@app.on_event("startup")
async def startup_event_consumers():
    # Start event consumers in background tasks
    #asyncio.create_task(domain_events.start_consumer())
    #asyncio.create_task(application_events.start_consumer())
    app.state.event_consumers_running = True
    print("Event consumers started")

@app.on_event("shutdown")
async def shutdown_event_consumers():
    # Event consumers will be stopped when their tasks are cancelled
    app.state.event_consumers_running = False
    print("Event consumers stopped")"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)