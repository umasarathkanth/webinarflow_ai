from typing import List

from pydantic import BaseModel


class SpeakerNotes(BaseModel):

    notes: List[str] = []


class SlideSpec(BaseModel):

    slide_number: int

    title: str

    content: List[str]

    layout_type: str

    image_required: bool = False

    image_prompt: str | None = None

    speaker_notes: SpeakerNotes