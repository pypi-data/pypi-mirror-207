from pydantic import BaseModel
from .colors import Colors


class GraphConfig(BaseModel):
    id: str = None
    name: str = None
    unit: str = None
    type: str = 0
    color: Colors = ''
