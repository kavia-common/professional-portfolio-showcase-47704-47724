import os
from functools import lru_cache
from pydantic import BaseModel, Field


class AppMeta(BaseModel):
    """Application metadata for FastAPI docs."""
    title: str = Field(default="Portfolio API", description="API title for OpenAPI")
    description: str = Field(
        default="REST API for portfolio projects, profile, skills, and assets.",
        description="API description for OpenAPI",
    )
    version: str = Field(default="1.0.0", description="API version for OpenAPI")


class CORSSettings(BaseModel):
    """CORS configuration with environment override."""
    allow_origins: list[str] = Field(default_factory=lambda: ["*"], description="Allowed origins")
    allow_credentials: bool = Field(default=True, description="Allow credentials")
    allow_methods: list[str] = Field(default_factory=lambda: ["*"], description="Allowed methods")
    allow_headers: list[str] = Field(default_factory=lambda: ["*"], description="Allowed headers")


class Settings(BaseModel):
    """Application settings loaded from environment."""
    meta: AppMeta = Field(default_factory=AppMeta)
    cors: CORSSettings = Field(default_factory=CORSSettings)
    api_prefix: str = Field(default="/api/v1", description="Versioned API prefix")


# PUBLIC_INTERFACE
@lru_cache()
def get_settings() -> Settings:
    """Return cached settings loaded from environment variables."""
    cors_origins = os.getenv("CORS_ALLOW_ORIGINS", "*")
    # Parse comma-separated list; empty treated as "*"
    origins = [o.strip() for o in cors_origins.split(",")] if cors_origins else ["*"]

    title = os.getenv("APP_TITLE", "Portfolio API")
    description = os.getenv(
        "APP_DESCRIPTION",
        "REST API for portfolio projects, profile, skills, and assets.",
    )
    version = os.getenv("APP_VERSION", "1.0.0")
    api_prefix = os.getenv("API_PREFIX", "/api/v1")

    return Settings(
        meta=AppMeta(title=title, description=description, version=version),
        cors=CORSSettings(allow_origins=origins),
        api_prefix=api_prefix,
    )
