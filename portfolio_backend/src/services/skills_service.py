from __future__ import annotations
from typing import List
from ..models import Skill
from ..storage.types import Repository


class SkillsService:
    """Service layer for skills operations."""

    def __init__(self, repo: Repository) -> None:
        self.repo = repo

    # PUBLIC_INTERFACE
    def list(self) -> List[Skill]:
        """Return list of skills."""
        return self.repo.list_skills()

    # PUBLIC_INTERFACE
    def add(self, skill: Skill) -> Skill:
        """Add a skill."""
        return self.repo.add_skill(skill)

    # PUBLIC_INTERFACE
    def delete(self, name: str) -> bool:
        """Delete a skill by name."""
        return self.repo.delete_skill(name)
