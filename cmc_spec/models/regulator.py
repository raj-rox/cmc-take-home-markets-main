"""A regulator: the body that grants licences and receives filings, acting for one or more markets."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from cmc_spec.core import DataModel, ImmutableSet, Reference, ReferenceCode, Strid, reference_data
from cmc_spec.models.market import MarketRef


class RegulatorCode(ReferenceCode):
    """Codes are added with the seed rows in `data/regulators.py`."""


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
