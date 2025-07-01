from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

class DiscussionSchema(BaseModel):
    id_user: Optional[str] = None
    discussuionmassage: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
