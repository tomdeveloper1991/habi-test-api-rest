import enum
from typing import List, Optional
import pydantic

from application.model.property import Property


class PropertyStateFilter(enum.Enum):
    PRE_SALE = "pre_venta"
    ON_SALE = "en_venta"
    SOLD = "vendido"


class RequestPropertyDto(pydantic.BaseModel):
    state: PropertyStateFilter
    city: Optional[str]
    year: Optional[str]

    class Config:
        use_enum_values = True


class ResponsePropertyDto(pydantic.BaseModel):
    property_result: List[Property]
