from __future__ import annotations
from typing import List, Optional
from ..models import Asset, AssetCreate
from ..storage.types import Repository


class AssetsService:
    """Service layer for asset metadata operations."""

    def __init__(self, repo: Repository) -> None:
        self.repo = repo

    # PUBLIC_INTERFACE
    def list(self) -> List[Asset]:
        """Return list of assets."""
        return self.repo.list_assets()

    # PUBLIC_INTERFACE
    def get(self, asset_id: str) -> Optional[Asset]:
        """Return an asset by id."""
        return self.repo.get_asset(asset_id)

    # PUBLIC_INTERFACE
    def create(self, data: AssetCreate, *, filename: str | None, content_type: str | None, size_bytes: int | None) -> Asset:
        """Create an asset metadata entry."""
        return self.repo.create_asset(data, filename=filename, content_type=content_type, size_bytes=size_bytes)
