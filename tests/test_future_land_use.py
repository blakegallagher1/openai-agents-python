from ebr_zoning_strategist.engine import ScenarioEngine
from ebr_zoning_strategist.models import FutureLandUseCategory, Parcel


def test_categories_loaded():
    assert FutureLandUseCategory.AGRICULTURAL_RURAL.value == "Agricultural/Rural"
    assert FutureLandUseCategory.COMMERCIAL.value == "Commercial"


def test_scenario_engine():
    engine = ScenarioEngine()
    parcel = Parcel(
        parcel_id="1",
        zoning_district="A1",
        proposed_use="residential",
        future_land_use=FutureLandUseCategory.AGRICULTURAL_RURAL,
    )
    report = engine.analyze(parcel)
    assert report.zoning_compliant is True
    assert report.future_land_use_compliant is True
