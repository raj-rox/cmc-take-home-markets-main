"""A licence: a product's authorisation from one regulator, covering one or more markets."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from cmc_spec.core import DataModel, ImmutableSet, Reference, Strid
from cmc_spec.models.market import MarketRef
from cmc_spec.models.product import ProductRef
from cmc_spec.models.regulator import RegulatorRef


class Licence(DataModel):
    """One licence. An EU centralised licence is one row covering every market it reaches.

    Invariants checked against other records:
    - every market is one the regulator acts for;
    - a product has at most one licence covering any market;
    - all its markets share one rule set for the product's type, or none of them has one.

    Its rule set is computed from its markets and the product's type, never stored.
    """

    product_strid: ProductRef
    regulator_strid: RegulatorRef
    market_strids: ImmutableSet[MarketRef] = Field(min_length=1)


LicenceRef = Annotated[Strid, Reference(Licence)]
