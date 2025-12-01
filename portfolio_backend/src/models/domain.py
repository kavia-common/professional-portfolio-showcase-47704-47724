from __future__ import annotations

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl


class ProjectBase(BaseModel):
    """Base schema for project shared fields."""
    title: str = Field(..., description="Project title")
    description: str = Field(..., description="Short project description")
    url: Optional[HttpUrl] = Field(default=None, description="Link to project demo or site")
    repo_url: Optional[HttpUrl] = Field(default=None, description="Link to project repository")
    tags: List[str] = Field(default_factory=list, description="List of associated tags")


class ProjectCreate(ProjectBase):
    """Schema for creating a new project."""
    pass


class ProjectUpdate(BaseModel):
    """Schema for updating a project."""
    title: Optional[str] = Field(default=None, description="Project title")
    description: Optional[str] = Field(default=None, description="Short project description")
    url: Optional[HttpUrl] = Field(default=None, description="Link to project demo or site")
    repo_url: Optional[HttpUrl] = Field(default=None, description="Link to project repository")
    tags: Optional[List[str]] = Field(default=None, description="List of associated tags")


class Project(ProjectBase):
    """Schema representing a persisted project."""
    id: str = Field(..., description="Unique project identifier")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")


class Profile(BaseModel):
    """Schema representing the portfolio owner profile."""
    name: str = Field(..., description="Full name")
    headline: str = Field(..., description="Short headline or role")
    bio: str = Field(..., description="Longer biography")
    email: Optional[str] = Field(default=None, description="Contact email")
    location: Optional[str] = Field(default=None, description="Location")
    website: Optional[HttpUrl] = Field(default=None, description="Personal website URL")


class ProfileUpdate(BaseModel):
    """Schema for updating the profile."""
    name: Optional[str] = Field(default=None, description="Full name")
    headline: Optional[str] = Field(default=None, description="Short headline or role")
    bio: Optional[str] = Field(default=None, description="Biography")
    email: Optional[str] = Field(default=None, description="Contact email")
    location: Optional[str] = Field(default=None, description="Location")
    website: Optional[HttpUrl] = Field(default=None, description="Personal website URL")


class Skill(BaseModel):
    """Schema representing a skill with optional level."""
    name: str = Field(..., description="Skill name")
    level: Optional[int] = Field(default=None, ge=1, le=10, description="Proficiency level 1-10")


class AssetCreate(BaseModel):
    """Schema for creating an asset from either upload or URL."""
    url: Optional[HttpUrl] = Field(default=None, description="Remote URL to reference asset")
    title: Optional[str] = Field(default=None, description="Optional human friendly title")
    description: Optional[str] = Field(default=None, description="Optional description text")


class Asset(BaseModel):
    """Schema representing stored asset metadata (in-memory)."""
    id: str = Field(..., description="Unique asset identifier")
    filename: Optional[str] = Field(default=None, description="Original filename if uploaded")
    content_type: Optional[str] = Field(default=None, description="MIME type")
    size_bytes: Optional[int] = Field(default=None, description="Size of uploaded file")
    url: Optional[HttpUrl] = Field(default=None, description="Remote URL if provided")
    title: Optional[str] = Field(default=None, description="Optional title")
    description: Optional[str] = Field(default=None, description="Optional description")
    created_at: datetime = Field(..., description="Creation timestamp")
