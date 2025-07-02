from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

class BorrowingSchema(BaseModel):
    id_user: Optional[str] = None
    id_book: Optional[str] = None
    id_payment: Optional[str] = None
    id_return: Optional[str] = None
    status: Literal["dipinjam", "selesai", "menunggu perstujuan", "dibatalkan", "ditolak"] = "dipinjam"
    duration: Optional[int] = None  # Duration in days

    model_config = ConfigDict(from_attributes=True)