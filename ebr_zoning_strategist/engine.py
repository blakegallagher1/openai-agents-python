from __future__ import annotations

from typing import Dict

from pydantic import BaseModel

from .models import FutureLandUseCategory, Parcel, ParcelReport

# Example zoning rules linking zoning districts to allowed future land use categories
ZONING_RULES: Dict[str, FutureLandUseCategory] = {
    "A1": FutureLandUseCategory.AGRICULTURAL_RURAL,
    "C1": FutureLandUseCategory.COMMERCIAL,
    "CN": FutureLandUseCategory.COMPACT_NEIGHBORHOOD,
}


class ScenarioEngine(BaseModel):
    """Simple scenario engine checking zoning and future land use compliance."""

    def analyze(self, parcel: Parcel) -> ParcelReport:
        details: Dict[str, str] = {}
        allowed_flu = ZONING_RULES.get(parcel.zoning_district)
        zoning_compliant = parcel.proposed_use.lower() in {"residential", "commercial", "agricultural"}
        if not zoning_compliant:
            details["zoning"] = f"Use '{parcel.proposed_use}' not allowed in zoning district {parcel.zoning_district}"

        flu_compliant = True
        if allowed_flu and parcel.future_land_use != allowed_flu:
            flu_compliant = False
            details["future_land_use"] = (
                f"Parcel future land use {parcel.future_land_use.value} does not match allowed category {allowed_flu.value}"
            )
        elif allowed_flu is None:
            flu_compliant = False
            details["future_land_use"] = f"Unknown zoning district {parcel.zoning_district}"

        return ParcelReport(
            parcel_id=parcel.parcel_id,
            zoning_compliant=zoning_compliant,
            future_land_use_compliant=flu_compliant,
            details=details,
        )
