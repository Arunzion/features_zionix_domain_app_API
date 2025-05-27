from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

# Create engine
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def init_db():
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        
        # Verify tables exist
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema='public'
            """))
            tables = [row[0] for row in result]
            logger.info(f"Created tables: {tables}")
            
        return True
    except Exception as e:
        logger.error(f"Database initialization error: {e}")
        raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()