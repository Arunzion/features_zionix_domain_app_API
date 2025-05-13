from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class DomainBase(BaseModel):
    domain_name: str = Field(..., alias="domain_name", min_length=3, max_length=100)
    domain_code: str = Field(..., alias="domain_code", min_length=3, max_length=50)
    description: Optional[str] = Field(None, alias="description")
    status: Optional[bool] = Field(True, alias="status")
    action: Optional[str] = Field(None, alias="action")

class DomainCreate(DomainBase):
    pass

class DomainUpdate(BaseModel):
    domain_name: Optional[str] = Field(None, alias="domain_name", min_length=3, max_length=100)
    domain_code: Optional[str] = Field(None, alias="domain_code", min_length=3, max_length=50)
    description: Optional[str] = Field(None, alias="description")
    status: Optional[bool] = Field(None, alias="status")
    action: Optional[str] = Field(None, alias="action")

class DomainResponse(DomainBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
