from typing import List, Optional
from pydantic import BaseModel

class BagLimit(BaseModel):
    hand_height: int
    hand_length: int
    hand_weight: int
    hand_width: int
    hold_dimensions_sum: int
    hold_height: int
    hold_length: int
    hold_weight: int
    hold_width: int
    personal_item_height: int
    personal_item_length: int
    personal_item_weight: int
    personal_item_width: int

class Conversion(BaseModel):
    EUR: float
    USD: float

class Country(BaseModel):
    code: str
    name: str

class Fare(BaseModel):
    adults: int
    children: int
    infants: int

class FareLocks(BaseModel):
    EUR: List[dict]
    USD: List[dict]

class Route(BaseModel):
    airline: str
    bags_recheck_required: bool
    cityCodeFrom: str
    cityCodeTo: str
    cityFrom: str
    cityTo: str
    combination_id: str
    equipment: Optional[str]
    fare_basis: str
    fare_category: str
    fare_classes: str
    flight_no: int
    flyFrom: str
    flyTo: str
    guarantee: bool
    id: str
    local_arrival: str
    local_departure: str
    operating_carrier: str
    operating_flight_no: str
    utc_arrival: str
    utc_departure: str
    vehicle_type: str
    vi_connection: bool

class FlightDetail(BaseModel):
    airlines: List[str]
    availability: dict
    baglimit: BagLimit
    booking_token: str
    cityCodeFrom: str
    cityCodeTo: str
    cityFrom: str
    cityTo: str
    conversion: Conversion
    countryFrom: Country
    countryTo: Country
    deep_link: str
    distance: float
    duration: dict
    facilitated_booking_available: bool
    fare: Fare
    fare_locks: FareLocks
    flyFrom: str
    flyTo: str
    has_airport_change: bool
    hidden_city_ticketing: bool
    id: str
    local_arrival: str
    local_departure: str
    nightsInDest: int
    pnr_count: int
    price: int
    quality: float
    route: List[Route]
    technical_stops: int
    throw_away_ticketing: bool
    utc_arrival: str
    utc_departure: str
    virtual_interlining: bool
