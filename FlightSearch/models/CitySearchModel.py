from typing import List, Optional, Dict, Union
from pydantic import BaseModel


class AlternativeDeparturePoint(BaseModel):
    distance: float
    duration: float
    id: str


class Continent(BaseModel):
    code: str
    id: str
    name: str
    slug: str


class Country(BaseModel):
    code: str
    id: str
    name: str
    slug: str


class Location(BaseModel):
    lat: float
    lon: float


class Region(BaseModel):
    id: str
    name: str
    slug: str


class Subdivision(BaseModel):
    code: str
    id: str
    name: str
    slug: str


class Tag(BaseModel):
    month_from: int
    month_to: int
    tag: str


class LocationDetail(BaseModel):
    active: bool
    airports: int
    alternative_departure_points: List[AlternativeDeparturePoint]
    alternative_names: List[str]
    autonomous_territory: Optional[str]
    bus_stations: int
    car_rentals: List[Dict[str, Union[int, List[str]]]]
    code: str
    continent: Continent
    country: Country
    dst_popularity_score: float
    global_rank_dst: int
    hotels: int
    id: str
    location: Location
    name: str
    nearby_country: Optional[str]
    population: int
    providers: List[int]
    rank: int
    region: Region
    slug: str
    slug_en: str
    stations: int
    subdivision: Subdivision
    tags: List[Tag]
    timezone: str
    type: str


class Meta(BaseModel):
    locale: Dict[str, str]


class CitySearchModel(BaseModel):
    last_refresh: int
    locations: List[LocationDetail]
    meta: Meta
    results_retrieved: int
