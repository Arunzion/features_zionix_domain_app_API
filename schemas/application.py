from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ApplicationBase(BaseModel):
    application_name: str = Field(..., min_length=3, max_length=100)  # Valid and descriptive name
    application_code: str = Field(..., min_length=3, max_length=50)  # Valid and descriptive name
    description: Optional[str] = None
    is_active: Optional[bool] = Field(True, alias="status")  # Changed `status` to `is_active` for clarity
    action: Optional[str] = None
    domain_name: str = Field(..., min_length=3, max_length=100)  # Clear and valid name
    config: Optional[str] = None  # JSON stored as text

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    application_name: Optional[str] = Field(None, min_length=3, max_length=100)
    application_code: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = Field(None, alias="status")  # Updated field
    action: Optional[str] = None
    domain_name: Optional[str] = Field(None, min_length=3, max_length=100)
    config: Optional[str] = None

class ApplicationResponse(ApplicationBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
