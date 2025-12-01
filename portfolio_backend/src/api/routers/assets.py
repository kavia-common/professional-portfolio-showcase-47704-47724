from typing import List, Optional
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from ...models import Asset, AssetCreate
from ...services.assets_service import AssetsService
from ...core.dependencies import get_assets_service

router = APIRouter(
    prefix="/assets",
    tags=["Assets"],
)


@router.get(
    "",
    response_model=List[Asset],
    summary="List assets",
    description="Return list of asset metadata entries.",
)
def list_assets(svc: AssetsService = Depends(get_assets_service)) -> List[Asset]:
    """List all asset metadata entries."""
    return svc.list()


@router.get(
    "/{asset_id}",
    response_model=Asset,
    responses={404: {"description": "Asset not found"}},
    summary="Get asset",
    description="Return an asset metadata by id.",
)
def get_asset(asset_id: str, svc: AssetsService = Depends(get_assets_service)) -> Asset:
    """Get asset by id."""
    asset = svc.get(asset_id)
    if not asset:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found")
    return asset


@router.post(
    "",
    response_model=Asset,
    status_code=status.HTTP_201_CREATED,
    summary="Create asset",
    description=(
        "Create an asset metadata entry. Either upload a file as multipart/form-data "
        "with 'file' field, or provide a JSON body with a 'url'. This endpoint stores metadata only."
    ),
)
async def create_asset(
    svc: AssetsService = Depends(get_assets_service),
    file: Optional[UploadFile] = File(default=None),
    url: Optional[str] = Form(default=None),
    title: Optional[str] = Form(default=None),
    description: Optional[str] = Form(default=None),
) -> Asset:
    """Create an asset metadata entry from either file upload or remote URL."""
    if not file and not url:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Provide either a file upload or a url")

    filename = None
    content_type = None
    size_bytes: Optional[int] = None

    if file:
        filename = file.filename
        content_type = file.content_type
        # We do not store file content; read to compute size only
        data = await file.read()
        size_bytes = len(data)

    payload = AssetCreate(url=url, title=title, description=description)
    return svc.create(payload, filename=filename, content_type=content_type, size_bytes=size_bytes)
