from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.session import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    application_name = Column(String(100), index=True, nullable=False)  # Changed from `name` to `application_name`
    application_code = Column(String(50), unique=True, index=True, nullable=False)  # Added as `Application code`
    description = Column(Text, nullable=True)
    status = Column(Boolean, default=True)  # Changed from `is_active` to `status`
    action = Column(String(50), nullable=True)  # Added `action` field
    domain_name = Column(String(100), ForeignKey("domains.domain_name"), nullable=False)  # Changed to `domain_name` as ForeignKey
    config = Column(Text, nullable=True)  # JSON stored as text
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    domain = relationship("Domain", back_populates="applications")

    def __repr__(self):
        return f"<Application {self.application_name}>"
