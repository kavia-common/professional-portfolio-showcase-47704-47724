from functools import lru_cache
from fastapi import Depends

from ..storage.memory_repo import InMemoryRepository
from ..services.projects_service import ProjectsService
from ..services.profile_service import ProfileService
from ..services.skills_service import SkillsService
from ..services.assets_service import AssetsService


# PUBLIC_INTERFACE
@lru_cache()
def get_repo() -> InMemoryRepository:
    """Return a singleton in-memory repository instance for the app lifetime."""
    return InMemoryRepository()


# PUBLIC_INTERFACE
def get_projects_service(repo: InMemoryRepository = Depends(get_repo)) -> ProjectsService:
    """FastAPI dependency to provide ProjectsService."""
    return ProjectsService(repo)


# PUBLIC_INTERFACE
def get_profile_service(repo: InMemoryRepository = Depends(get_repo)) -> ProfileService:
    """FastAPI dependency to provide ProfileService."""
    return ProfileService(repo)


# PUBLIC_INTERFACE
def get_skills_service(repo: InMemoryRepository = Depends(get_repo)) -> SkillsService:
    """FastAPI dependency to provide SkillsService."""
    return SkillsService(repo)


# PUBLIC_INTERFACE
def get_assets_service(repo: InMemoryRepository = Depends(get_repo)) -> AssetsService:
    """FastAPI dependency to provide AssetsService."""
    return AssetsService(repo)
