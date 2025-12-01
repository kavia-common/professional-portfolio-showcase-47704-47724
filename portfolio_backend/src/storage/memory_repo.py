from __future__ import annotations

import uuid
from datetime import datetime
from typing import Dict, List, Optional

from .types import Repository
from ..models import (
    Project,
    ProjectCreate,
    ProjectUpdate,
    Profile,
    ProfileUpdate,
    Skill,
    Asset,
    AssetCreate,
)


class InMemoryRepository(Repository):
    """Simple in-memory store for portfolio data. Not persistent."""

    def __init__(self) -> None:
        # Projects storage
        self._projects: Dict[str, Project] = {}
        # Profile, initialize with defaults
        self._profile: Profile = Profile(
            name="Your Name",
            headline="Software Developer",
            bio="Welcome to my portfolio!",
            email=None,
            location=None,
            website=None,
        )
        # Skills storage
        self._skills: Dict[str, Skill] = {}
        # Assets storage
        self._assets: Dict[str, Asset] = {}

    # Projects
    def list_projects(self) -> List[Project]:
        return list(self._projects.values())

    def get_project(self, project_id: str) -> Optional[Project]:
        return self._projects.get(project_id)

    def create_project(self, data: ProjectCreate) -> Project:
        now = datetime.utcnow()
        pid = str(uuid.uuid4())
        project = Project(
            id=pid,
            title=data.title,
            description=data.description,
            url=data.url,
            repo_url=data.repo_url,
            tags=data.tags or [],
            created_at=now,
            updated_at=now,
        )
        self._projects[pid] = project
        return project

    def update_project(self, project_id: str, data: ProjectUpdate) -> Optional[Project]:
        existing = self._projects.get(project_id)
        if not existing:
            return None
        updated = existing.model_copy(update={
            "title": data.title if data.title is not None else existing.title,
            "description": data.description if data.description is not None else existing.description,
            "url": data.url if data.url is not None else existing.url,
            "repo_url": data.repo_url if data.repo_url is not None else existing.repo_url,
            "tags": data.tags if data.tags is not None else existing.tags,
            "updated_at": datetime.utcnow(),
        })
        self._projects[project_id] = updated
        return updated

    def delete_project(self, project_id: str) -> bool:
        return self._projects.pop(project_id, None) is not None

    # Profile
    def get_profile(self) -> Profile:
        return self._profile

    def update_profile(self, data: ProfileUpdate) -> Profile:
        self._profile = self._profile.model_copy(update={
            k: v for k, v in data.model_dump(exclude_unset=True).items()
        })
        return self._profile

    # Skills
    def list_skills(self) -> List[Skill]:
        return list(self._skills.values())

    def add_skill(self, skill: Skill) -> Skill:
        self._skills[skill.name.lower()] = skill
        return skill

    def delete_skill(self, name: str) -> bool:
        key = name.lower()
        return self._skills.pop(key, None) is not None

    # Assets
    def list_assets(self) -> List[Asset]:
        return list(self._assets.values())

    def get_asset(self, asset_id: str) -> Optional[Asset]:
        return self._assets.get(asset_id)

    def create_asset(self, data: AssetCreate, *, filename: str | None, content_type: str | None, size_bytes: int | None) -> Asset:
        aid = str(uuid.uuid4())
        now = datetime.utcnow()
        asset = Asset(
            id=aid,
            filename=filename,
            content_type=content_type,
            size_bytes=size_bytes,
            url=data.url,
            title=data.title,
            description=data.description,
            created_at=now,
        )
        self._assets[aid] = asset
        return asset
