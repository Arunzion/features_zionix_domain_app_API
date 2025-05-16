from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class DomainBase(BaseModel):
    domain_name: str = Field(..., min_length=3, max_length=100)  # Valid name
    domain_code: str = Field(..., min_length=3, max_length=50)  # Valid name
    description: Optional[str] = None
    is_active: Optional[bool] = Field(True, alias="status")  # Renamed to `is_active`
    action: Optional[str] = None

class DomainCreate(DomainBase):
    pass

class DomainUpdate(BaseModel):
    domain_name: Optional[str] = Field(None, min_length=3, max_length=100)
    domain_code: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = Field(None, alias="status")  # Renamed to `is_active`
    action: Optional[str] = None

class DomainResponse(DomainBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
