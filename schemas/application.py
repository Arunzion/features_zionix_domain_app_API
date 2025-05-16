from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ApplicationBase(BaseModel):
    application_name: str = Field(..., min_length=3, max_length=100)  # Changed from `name`
    application_code: str = Field(..., min_length=3, max_length=50)   # Added as `Application code`
    description: Optional[str] = None
    status: Optional[bool] = True  # Changed from `is_active`
    action: Optional[str] = None  # Added `action`
    domain_name: str = Field(..., min_length=3, max_length=100)  # Changed from `domain_id` to `domain_name`
    config: Optional[str] = None  # JSON stored as text

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    application_name: Optional[str] = Field(None, min_length=3, max_length=100)  # Updated
    application_code: Optional[str] = Field(None, min_length=3, max_length=50)   # Added
    description: Optional[str] = None
    status: Optional[bool] = None  # Updated from `is_active`
    action: Optional[str] = None  # Added
    domain_name: Optional[str] = Field(None, min_length=3, max_length=100)  # Updated
    config: Optional[str] = None  # No changes

class ApplicationResponse(ApplicationBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
