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
    """Prefixed with the rule set, so categories sharing a label (EU `IB`, UK `IB`) stay distinct."""

    US_PAS = "US_PAS"
    US_CBE_30 = "US_CBE_30"
    US_CBE_0 = "US_CBE_0"
    US_AR = "US_AR"
    US_PQS_NOFILE = "US_PQS_NOFILE"
    US_BLA_PAS = "US_BLA_PAS"
    US_BLA_CBE_30 = "US_BLA_CBE_30"
    US_BLA_CBE_0 = "US_BLA_CBE_0"
    US_BLA_AR = "US_BLA_AR"
    US_BLA_PQS_NOFILE = "US_BLA_PQS_NOFILE"
    EU_IA = "EU_IA"
    EU_IA_IN = "EU_IA_IN"
    EU_IB = "EU_IB"
    EU_II = "EU_II"
    EU_EXT = "EU_EXT"
    EU_VACC = "EU_VACC"
    UK_IA = "UK_IA"
    UK_IA_IN = "UK_IA_IN"
    UK_IB = "UK_IB"
    UK_II = "UK_II"
    UK_EXT = "UK_EXT"
    CH_IA = "CH_IA"
    CH_IA_IN = "CH_IA_IN"
    CH_IB = "CH_IB"
    CH_II = "CH_II"
    CH_EXT = "CH_EXT"
    SA_IA = "SA_IA"
    SA_IA_IN = "SA_IA_IN"
    SA_IB = "SA_IB"
    SA_II = "SA_II"
    SA_NEW_APP = "SA_NEW_APP"
    ZA_IA = "ZA_IA"
    ZA_IA_IN = "ZA_IA_IN"
    ZA_IB = "ZA_IB"
    ZA_II = "ZA_II"
    ZA_EXT = "ZA_EXT"
    ZA_EDITORIAL = "ZA_EDITORIAL"
    SG_MAV_1 = "SG_MAV_1"
    SG_MAV_2 = "SG_MAV_2"
    SG_MIV_1 = "SG_MIV_1"
    SG_MIV_2_NOTIFICATION = "SG_MIV_2_NOTIFICATION"
    SG_MIV_2_DO_AND_TELL = "SG_MIV_2_DO_AND_TELL"
    SG_NO_NOTIFICATION = "SG_NO_NOTIFICATION"
    MY_MAV = "MY_MAV"
    MY_MIV_PA = "MY_MIV_PA"
    MY_MIV_PA_TELL_AND_DO = "MY_MIV_PA_TELL_AND_DO"
    MY_MIV_N = "MY_MIV_N"
    PH_MAV = "PH_MAV"
    PH_MIV_PA = "PH_MIV_PA"
    PH_MIV_N = "PH_MIV_N"
    ID_VARIASI_MAJOR = "ID_VARIASI_MAJOR"
    ID_VARIASI_MINOR = "ID_VARIASI_MINOR"
    ID_VARIASI_NOTIFIKASI = "ID_VARIASI_NOTIFIKASI"
    VN_MAV = "VN_MAV"
    VN_MIV_PA = "VN_MIV_PA"
    VN_MIV_N = "VN_MIV_N"
    CN_SUPP = "CN_SUPP"
    CN_REC = "CN_REC"
    CN_AR = "CN_AR"
    BR_SYN_HMP = "BR_SYN_HMP"
    BR_SYN_II_PROT = "BR_SYN_II_PROT"
    BR_SYN_PA = "BR_SYN_PA"
    BR_BIO_MAIOR = "BR_BIO_MAIOR"
    BR_BIO_MOD = "BR_BIO_MOD"
    BR_BIO_MENOR = "BR_BIO_MENOR"
    MX_MCRS_MENOR = "MX_MCRS_MENOR"
    MX_MCRS_MODERADA = "MX_MCRS_MODERADA"
    MX_MCRS_MAYOR = "MX_MCRS_MAYOR"
    AR_MOD_PREV = "AR_MOD_PREV"
    AR_MOD_NOTIF = "AR_MOD_NOTIF"


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
