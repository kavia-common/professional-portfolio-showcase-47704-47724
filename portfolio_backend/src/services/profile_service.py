from __future__ import annotations
from ..models import Profile, ProfileUpdate
from ..storage.types import Repository


class ProfileService:
    """Service layer for profile operations."""

    def __init__(self, repo: Repository) -> None:
        self.repo = repo

    # PUBLIC_INTERFACE
    def get(self) -> Profile:
        """Return the profile."""
        return self.repo.get_profile()

    # PUBLIC_INTERFACE
    def update(self, data: ProfileUpdate) -> Profile:
        """Update the profile."""
        return self.repo.update_profile(data)
