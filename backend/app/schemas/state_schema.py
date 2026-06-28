from typing import Optional

from pydantic import BaseModel

from app.schemas.slide_schema import SlideSpec


class ResearchCard(BaseModel):

    source: str

    summary: str

    confidence: float


class PPTState(BaseModel):

    topic: str

    duration_minutes: Optional[int] = None

    slide_count: Optional[int] = None

    audience: str

    tone: str

    template_id: str

    subtopics: list[str] = []

    research_cards: list[ResearchCard] = []

    outline: list[str] = []

    slide_specs: list[SlideSpec] = []

    image_assets: list[str] = []

    quality_report: dict = {}

    pptx_path: str | None = None