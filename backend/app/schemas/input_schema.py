from typing import Optional
from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=5,
        max_length=300
    )

    duration_minutes: Optional[int] = Field(
        default=None,
        ge=5,
        le=240
    )

    slide_count: Optional[int] = Field(
        default=None,
        ge=3,
        le=60
    )

    audience: str

    tone: str

    template_id: str
    
    
class GenerateResponse(BaseModel):

    success: bool

    project_id: str

    status: str

    message: str

    pptx_path: str | None = None