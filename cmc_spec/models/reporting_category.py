"""A reporting category: one category within one rule set, and the filing route it requires."""

from __future__ import annotations

from typing import Annotated

from cmc_spec.core import DataModel, Reference, ReferenceCode, Strid, reference_data
from cmc_spec.models.rule_set import RuleSetRef


class FilingRoute(ReferenceCode):
    """What a category requires, by when the change may be implemented relative to telling the regulator."""

    PRIOR_APPROVAL = "PRIOR_APPROVAL"
    """File first; implement only once the regulator approves."""
    NOTIFY_THEN_WAIT = "NOTIFY_THEN_WAIT"
    """File first; implement after a set standstill unless the regulator objects."""
    NOTIFY_AT_IMPLEMENTATION = "NOTIFY_AT_IMPLEMENTATION"
    """Implement, then file an individual notification at once or within a set window."""
    DO_AND_DOCUMENT = "DO_AND_DOCUMENT"
    """Implement and record; report only in a periodic, bundled filing or the company's own change history."""
    NO_FILING = "NO_FILING"
    """Never reported to the regulator."""
    NEW_APPLICATION = "NEW_APPLICATION"
    """Can't be filed as a variation; needs an extension or new licence application."""


class ReportingCategoryCode(ReferenceCode):
    """Prefixed with the rule set, so categories sharing a label (EU `IB`, UK `IB`) stay distinct.

    Codes are added with the seed rows in `data/reporting_categories.py`.
    """


@reference_data
class ReportingCategory(DataModel):
    """A category a change can be classified into. Seeded in `data/reporting_categories.py`.

    `label` is the code as the rule set prints it (`IB`, `MIV-1`). It is unique within its rule set,
    not across rule sets.
    """

    code: ReportingCategoryCode
    label: str
    name: str
    rule_set_strid: RuleSetRef
    filing_route: FilingRoute


ReportingCategoryRef = Annotated[Strid, Reference(ReportingCategory)]
