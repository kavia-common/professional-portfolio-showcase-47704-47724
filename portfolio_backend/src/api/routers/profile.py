from fastapi import APIRouter, Depends
from ...models import Profile, ProfileUpdate
from ...services.profile_service import ProfileService
from ...core.dependencies import get_profile_service

router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)


@router.get(
    "",
    response_model=Profile,
    summary="Get profile",
    description="Return the portfolio owner profile.",
)
def get_profile(svc: ProfileService = Depends(get_profile_service)) -> Profile:
    """Return the profile."""
    return svc.get()


@router.put(
    "",
    response_model=Profile,
    summary="Update profile",
    description="Update the portfolio owner profile.",
)
def update_profile(payload: ProfileUpdate, svc: ProfileService = Depends(get_profile_service)) -> Profile:
    """Update the profile."""
    return svc.update(payload)
