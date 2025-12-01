from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from ...models import Skill
from ...services.skills_service import SkillsService
from ...core.dependencies import get_skills_service

router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
)


@router.get(
    "",
    response_model=List[Skill],
    summary="List skills",
    description="Return a list of skills.",
)
def list_skills(svc: SkillsService = Depends(get_skills_service)) -> List[Skill]:
    """List skills."""
    return svc.list()


@router.post(
    "",
    response_model=Skill,
    status_code=status.HTTP_201_CREATED,
    summary="Add skill",
    description="Add a new skill.",
)
def add_skill(payload: Skill, svc: SkillsService = Depends(get_skills_service)) -> Skill:
    """Add a new skill."""
    return svc.add(payload)


@router.delete(
    "/{name}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "Skill not found"}},
    summary="Delete skill",
    description="Delete a skill by name.",
)
def delete_skill(name: str, svc: SkillsService = Depends(get_skills_service)) -> None:
    """Delete a skill by name."""
    deleted = svc.delete(name)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found")
    return None
