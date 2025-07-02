from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

class PaymentSchema(BaseModel):
    id_user: Optional[str] = None
    id_borrowing: Optional[str] = None
    payment_date: Optional[datetime] = None
    payment_method: Literal["QRIS"] = "QRIS"
    payment_totalprice: Optional[int] = None  # Total price in cents

    model_config = ConfigDict(from_attributes=True)