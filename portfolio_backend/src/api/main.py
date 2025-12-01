from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..core.config import get_settings
from .routers.projects import router as projects_router
from .routers.profile import router as profile_router
from .routers.skills import router as skills_router
from .routers.assets import router as assets_router

settings = get_settings()

openapi_tags = [
    {"name": "Projects", "description": "Operations with portfolio projects"},
    {"name": "Profile", "description": "Profile information management"},
    {"name": "Skills", "description": "Skills management"},
    {"name": "Assets", "description": "Asset metadata management"},
]

app = FastAPI(
    title=settings.meta.title,
    description=settings.meta.description,
    version=settings.meta.version,
    openapi_tags=openapi_tags,
)

# CORS setup based on env
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.allow_origins,
    allow_credentials=settings.cors.allow_credentials,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
)


@app.get("/", summary="Health Check", tags=["Profile"])
def health_check():
    """Health check endpoint returning basic service status."""
    return {"message": "Healthy"}


# Mount API v1 routers under configured prefix
api_prefix = settings.api_prefix
app.include_router(projects_router, prefix=api_prefix)
app.include_router(profile_router, prefix=api_prefix)
app.include_router(skills_router, prefix=api_prefix)
app.include_router(assets_router, prefix=api_prefix)
