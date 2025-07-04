from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

class PickUpSchema(BaseModel):
    borrow_date: Optional[datetime] = None   
    image_pickup_url: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)