from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ...models import Project, ProjectCreate, ProjectUpdate
from ...services.projects_service import ProjectsService
from ...core.dependencies import get_projects_service

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get(
    "",
    response_model=List[Project],
    summary="List projects",
    description="Return a list of all portfolio projects.",
)
def list_projects(svc: ProjectsService = Depends(get_projects_service)) -> List[Project]:
    """List all projects."""
    return svc.list()


@router.get(
    "/{project_id}",
    response_model=Project,
    responses={404: {"description": "Project not found"}},
    summary="Get project",
    description="Return a project by its identifier.",
)
def get_project(project_id: str, svc: ProjectsService = Depends(get_projects_service)) -> Project:
    """Get a project by id."""
    project = svc.get(project_id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project


@router.post(
    "",
    response_model=Project,
    status_code=status.HTTP_201_CREATED,
    summary="Create project",
    description="Create a new project with title, description, and optional links.",
)
def create_project(payload: ProjectCreate, svc: ProjectsService = Depends(get_projects_service)) -> Project:
    """Create a project."""
    return svc.create(payload)


@router.put(
    "/{project_id}",
    response_model=Project,
    responses={404: {"description": "Project not found"}},
    summary="Update project",
    description="Update fields of an existing project.",
)
def update_project(project_id: str, payload: ProjectUpdate, svc: ProjectsService = Depends(get_projects_service)) -> Project:
    """Update a project by id."""
    updated = svc.update(project_id, payload)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return updated


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "Project not found"}},
    summary="Delete project",
    description="Delete an existing project by id.",
)
def delete_project(project_id: str, svc: ProjectsService = Depends(get_projects_service)) -> None:
    """Delete a project by id."""
    deleted = svc.delete(project_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return None
