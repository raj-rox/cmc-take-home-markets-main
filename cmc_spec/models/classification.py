"""A classification: what the user records for one licence on one change."""

from __future__ import annotations

from typing import Annotated, Self

from pydantic import Field, model_validator

from cmc_spec.core import DataModel, Reference, Strid
from cmc_spec.models.change import ChangeRef
from cmc_spec.models.licence import LicenceRef
from cmc_spec.models.reporting_category import FilingRoute, ReportingCategoryRef


class Classification(DataModel):
    """One licence on one change, shown once for each market the licence covers.

    - With a category: classified; the filing route is the category's.
    - With a filing route and no category: classified where the licence has no rule set.
    - With neither: not affected.
    A licence of an affected product with no classification is not yet classified.

    Invariants checked against other records:
    - one classification per change and licence;
    - the licence belongs to one of the change's products;
    - a category belongs to the licence's rule set;
    - a filing route without a category only where the licence has no rule set.
    """

    change_strid: ChangeRef
    licence_strid: LicenceRef
    reporting_category_strid: ReportingCategoryRef | None = None
    filing_route: FilingRoute | None = None
    reasoning: str = Field(min_length=1)

    @model_validator(mode="after")
    def _category_or_route(self) -> Self:
        if self.reporting_category_strid is not None and self.filing_route is not None:
            raise ValueError("record a category or a filing route, not both")
        return self


ClassificationRef = Annotated[Strid, Reference(Classification)]
