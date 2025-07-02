from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

class PickUpSchema(BaseModel):
    id_borrowing: Optional[str] = None   
    image: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)