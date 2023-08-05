from pydantic import BaseModel
from typing import Optional


class SdInpaintReqDto(BaseModel):
    image: str
    mask: str
    prompt: str
    device: Optional[str] = 'cpu'


class SdGenerateReqDto(BaseModel):
    prompt: str
    height: Optional[int] = 768
    width: Optional[int] = 1024
