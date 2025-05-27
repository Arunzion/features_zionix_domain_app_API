import os
from typing import List, Optional, Union
from pydantic import AnyHttpUrl, validator, SecretStr,model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "ZCare Admin Service"
    API_V1_STR: str = "/api/v1"
    
    # CORS settings
    CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    # Database settings
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "db")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "Arunnathan")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "admin_service")

    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def assemble_db_connection(cls, values):
        if not values.get("SQLALCHEMY_DATABASE_URI"):
            values["SQLALCHEMY_DATABASE_URI"] = (
                f"postgresql://{values.get('POSTGRES_USER')}:{values.get('POSTGRES_PASSWORD')}"
                f"@{values.get('POSTGRES_SERVER')}:{values.get('POSTGRES_PORT')}/{values.get('POSTGRES_DB')}"
            )
        return values
    # Kafka settings
    KAFKA_BOOTSTRAP_SERVERS: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    KAFKA_CONSUMER_GROUP: str = os.getenv("KAFKA_CONSUMER_GROUP", "admin-service")
    
    # Authentication settings
    AUTH_SERVICE_URL: str = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8000")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "supersecretkey")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    class Config:
        case_sensitive = True
        from_attributes = True
        env_file = ".env"

settings = Settings()