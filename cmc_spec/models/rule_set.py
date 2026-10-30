"""A rule set: a published scheme of reporting categories, applying in given markets to given product types."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from cmc_spec.core import DataModel, ImmutableSet, Reference, ReferenceCode, Strid, reference_data
from cmc_spec.models.market import MarketRef
from cmc_spec.models.product_type import ProductTypeRef


class RuleSetCode(ReferenceCode):
    US_CFR_314_70 = "US_CFR_314_70"
    EU_VARIATIONS = "EU_VARIATIONS"
    UK_VARIATIONS = "UK_VARIATIONS"
    CH_VARIATIONS = "CH_VARIATIONS"
    SA_VARIATIONS = "SA_VARIATIONS"
    ZA_VARIATIONS = "ZA_VARIATIONS"
    SG_HSA = "SG_HSA"
    MY_MVG = "MY_MVG"
    PH_PVG = "PH_PVG"
    ID_BPOM = "ID_BPOM"
    VN_DAV = "VN_DAV"
    CN_POST_APPROVAL = "CN_POST_APPROVAL"
    BR_RDC_73_2016 = "BR_RDC_73_2016"
    BR_RDC_913_2024 = "BR_RDC_913_2024"
    MX_MCRS = "MX_MCRS"
    AR_REM = "AR_REM"


@reference_data
class RuleSet(DataModel):
    """A scheme of reporting categories. Seeded in `data/rule_sets.py`.

    It applies to every pair of one of its markets and one of its product types. No two rule sets
    share a pair. A pair no rule set covers has no rule set recorded: "rule set unknown".

    `source` is the governing document and its current edition. Only the current edition is held;
    when it is replaced, the row is updated in place.
    """

    code: RuleSetCode
    name: str
    source: str
    market_strids: ImmutableSet[MarketRef] = Field(min_length=1)
    product_type_strids: ImmutableSet[ProductTypeRef] = Field(min_length=1)


RuleSetRef = Annotated[Strid, Reference(RuleSet)]
