from __future__ import annotations
from typing import List, Optional
from ..models import Project, ProjectCreate, ProjectUpdate
from ..storage.types import Repository


class ProjectsService:
    """Service layer for project operations."""

    def __init__(self, repo: Repository) -> None:
        self.repo = repo

    # PUBLIC_INTERFACE
    def list(self) -> List[Project]:
        """Return all projects."""
        return self.repo.list_projects()

    # PUBLIC_INTERFACE
    def get(self, project_id: str) -> Optional[Project]:
        """Get a project by id."""
        return self.repo.get_project(project_id)

    # PUBLIC_INTERFACE
    def create(self, data: ProjectCreate) -> Project:
        """Create a new project."""
        return self.repo.create_project(data)

    # PUBLIC_INTERFACE
    def update(self, project_id: str, data: ProjectUpdate) -> Optional[Project]:
        """Update a project by id."""
        return self.repo.update_project(project_id, data)

    # PUBLIC_INTERFACE
    def delete(self, project_id: str) -> bool:
        """Delete project by id. Returns True if deleted."""
        return self.repo.delete_project(project_id)
