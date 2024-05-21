from typing import List, Optional
from pydantic import BaseModel


class CityItem(BaseModel):
    city: str
    iataCode: Optional[str]
    id: int
    lowestPrice: int


class CitiesDataModel(BaseModel):
    cities: List[CityItem]


