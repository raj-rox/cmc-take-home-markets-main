"""A market: a country where a product can be licensed."""

from __future__ import annotations

from typing import Annotated

from cmc_spec.core import DataModel, Reference, ReferenceCode, Strid, reference_data


class MarketCode(ReferenceCode):
    """ISO 3166-1 alpha-2."""

    US = "US"
    DE = "DE"
    FR = "FR"
    NO = "NO"
    GB = "GB"
    CH = "CH"
    SA = "SA"
    ZA = "ZA"
    CN = "CN"
    BR = "BR"
    MX = "MX"
    AR = "AR"
    BN = "BN"
    KH = "KH"
    ID = "ID"
    LA = "LA"
    MY = "MY"
    MM = "MM"
    PH = "PH"
    SG = "SG"
    TH = "TH"
    TL = "TL"
    VN = "VN"


@reference_data
class Market(DataModel):
    """A country a licence can cover. Seeded in `data/markets.py`."""

    code: MarketCode
    name: str


MarketRef = Annotated[Strid, Reference(Market)]
