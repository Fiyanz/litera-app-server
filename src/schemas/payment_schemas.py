from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

class PaymentSchema(BaseModel):
    id_borrowing: Optional[str] = None
    id_pickup: Optional[str] = None  # ID for the pickup, if applicable
    payment_date: Optional[datetime] = None
    payment_method: Literal["QRIS"] = "QRIS"
    payment_totalprice: Optional[int] = None  # Total price in cents
    pickup_method: Literal["COD", "Ambil Ditempat"] = "COD"  # Default to COD

    model_config = ConfigDict(from_attributes=True)