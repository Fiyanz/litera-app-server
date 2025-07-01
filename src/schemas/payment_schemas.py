from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

class PaymentSchema(BaseModel):
    id_user: Optional[str] = None
    id_borrowing: Optional[str] = None
    payment_status: Literal["pending", "success", "failed"] = "pending"
    payment_amount: Optional[int] = None
    payment_details: Optional[str] = None
    payment_date: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)