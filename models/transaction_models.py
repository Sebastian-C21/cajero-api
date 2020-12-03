from pydantic import BaseModel
from datetime import datetime

class TrasanctionIn(BaseModel):
    username: str
    value: int

class TransactoinOut(BaseModel):
    id_transaction: int
    username: str
    date: datetime
    value: int
    actual_value: int