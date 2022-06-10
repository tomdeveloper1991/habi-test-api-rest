from typing import Optional
import pydantic


class Property(pydantic.BaseModel):
    id: int
    address: str
    city: str
    price: int
    description: Optional[str]
    year: Optional[int]
    status_name: Optional[str]
