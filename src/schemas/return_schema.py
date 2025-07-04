from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

class ReturnSchema(BaseModel):
    return_date: Optional[datetime] = None
    image: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)  # Enable attribute access