from pydantic import BaseModel
from typing import Optional


class SdInpaintReqDto(BaseModel):
    image: str
    mask: str
    prompt: str
    device: Optional[str] = 'cpu'
