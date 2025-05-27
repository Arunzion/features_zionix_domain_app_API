from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import logging
from contextlib import asynccontextmanager
from app.api.routes import domain, application
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
from app.db.session import init_db

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    try:
        logger.info("Starting database initialization...")
        init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Startup error: {e}")
        raise
    
    yield
    
    logger.info("Shutting down...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Admin Service API for ZCare Platform",
    version="0.1.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)