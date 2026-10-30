"""A regulator: the body that grants licences and receives filings, acting for one or more markets."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from cmc_spec.core import DataModel, ImmutableSet, Reference, ReferenceCode, Strid, reference_data
from cmc_spec.models.market import MarketRef


class RegulatorCode(ReferenceCode):
    FDA = "FDA"
    EC_EMA = "EC_EMA"
    BFARM = "BFARM"
    ANSM = "ANSM"
    NOMA = "NOMA"
    MHRA = "MHRA"
    SWISSMEDIC = "SWISSMEDIC"
    SFDA = "SFDA"
    SAHPRA = "SAHPRA"
    BDMCA = "BDMCA"
    KH_DDF = "KH_DDF"
    BPOM = "BPOM"
    LA_FDD = "LA_FDD"
    NPRA = "NPRA"
    MM_DFDA = "MM_DFDA"
    FDA_PH = "FDA_PH"
    HSA = "HSA"
    THAI_FDA = "THAI_FDA"
    TL_DNFM = "TL_DNFM"
    DAV = "DAV"
    NMPA = "NMPA"
    ANVISA = "ANVISA"
    COFEPRIS = "COFEPRIS"
    ANMAT = "ANMAT"


@reference_data
class Regulator(DataModel):
    """A body that grants licences. Seeded in `data/regulators.py`.

    `market_strids` are the markets it acts for: the European Commission acts for every EU and EEA
    market, BfArM for Germany alone.
    """

    code: RegulatorCode
    name: str
    market_strids: ImmutableSet[MarketRef] = Field(min_length=1)


RegulatorRef = Annotated[Strid, Reference(Regulator)]
