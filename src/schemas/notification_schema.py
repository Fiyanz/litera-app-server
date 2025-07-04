from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

class NotificationSchema(BaseModel):
    id_user: Optional[str] = None
    notification_message: Optional[str] = None
    created_at: Optional[datetime] = None
    is_read: Optional[bool] = False  # Default to False, indicating unread

    model_config = ConfigDict(from_attributes=True)