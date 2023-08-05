from pydantic import BaseModel


class ReturnBase(BaseModel):
    msg: str
    msgCode: str
    total: int
    data: object
