from pydantic import BaseModel


class UserConfig(BaseModel):
    token: str
