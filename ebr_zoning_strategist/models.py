from __future__ import annotations

import re
from enum import Enum
from pathlib import Path
from typing import Dict, List

from pydantic import BaseModel

CATEGORY_FILE = Path(__file__).resolve().parent.parent / "future land use categories.txt"


def _parse_categories(file_path: Path) -> List[str]:
    text = file_path.read_text(encoding="utf-8")
    pattern = re.compile(r"^([A-Za-z/ \-]+?)\s*\([A-Z/]+\)$", re.MULTILINE)
    return [m.group(1).strip() for m in pattern.finditer(text)]


FUTURE_LAND_USE_CATEGORIES: List[str] = _parse_categories(CATEGORY_FILE)


class FutureLandUseCategory(str, Enum):
    AGRICULTURAL_RURAL = "Agricultural/Rural"
    COMMERCIAL = "Commercial"
    COMPACT_NEIGHBORHOOD = "Compact Neighborhood"
    DOWNTOWN_CORE = "Downtown Core"
    EMPLOYMENT_CENTER = "Employment Center"
    INDUSTRIAL = "Industrial"
    INSTITUTIONAL = "Institutional"
    MIXED_USE = "Mixed-Use"
    NEIGHBORHOOD_CENTER = "Neighborhood Center"
    OFFICE = "Office"
    PARKS_AND_OPEN_SPACE = "Parks and Open Space"
    REGIONAL_CENTER = "Regional Center"
    RESIDENTIAL_NEIGHBORHOOD = "Residential Neighborhood"
    URBAN_NEIGHBORHOOD = "Urban Neighborhood"


class Parcel(BaseModel):
    parcel_id: str
    zoning_district: str
    proposed_use: str
    future_land_use: FutureLandUseCategory


class ParcelReport(BaseModel):
    parcel_id: str
    zoning_compliant: bool
    future_land_use_compliant: bool
    details: Dict[str, str]
