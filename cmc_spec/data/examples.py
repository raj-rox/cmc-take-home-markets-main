"""Example customer rows: one change, two products, their licences and classifications.

Not reference data. Licences and classifications are written by users, not seeded; these rows only
show the model handling the cases in the evidence. Each comment names the story it demonstrates.
"""

from __future__ import annotations

from cmc_spec.core import seed_strid
from cmc_spec.data.dosage_forms import DOSAGE_FORMS_BY_CODE
from cmc_spec.data.markets import MARKETS_BY_CODE
from cmc_spec.data.product_types import PRODUCT_TYPES_BY_CODE
from cmc_spec.data.regulators import REGULATORS_BY_CODE
from cmc_spec.data.reporting_categories import REPORTING_CATEGORIES_BY_CODE
from cmc_spec.models.change import Change
from cmc_spec.models.classification import Classification
from cmc_spec.models.dosage_form import DosageFormCode
from cmc_spec.models.licence import Licence
from cmc_spec.models.market import MarketCode
from cmc_spec.models.product import Product
from cmc_spec.models.product_type import ProductTypeCode
from cmc_spec.models.regulator import RegulatorCode
from cmc_spec.models.reporting_category import FilingRoute, ReportingCategoryCode

# Every product has a product type (AC2.7); it decides Brazil's and the US's rule set (AC2.2).
TABLET = Product(
    strid=seed_strid("example_product", "TABLET"),
    name="Examplinib 50 mg tablets",
    dosage_form_strid=DOSAGE_FORMS_BY_CODE[DosageFormCode.TABLET].strid,
    product_type_strid=PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid,
)
INJECTION = Product(
    strid=seed_strid("example_product", "INJECTION"),
    name="Examplimab 100 mg/mL solution for injection",
    dosage_form_strid=DOSAGE_FORMS_BY_CODE[DosageFormCode.SOLUTION_FOR_INJECTION].strid,
    product_type_strid=PRODUCT_TYPES_BY_CODE[ProductTypeCode.BIOLOGICAL].strid,
)

CHANGE = Change(
    strid=seed_strid("example_change", "NEW_SUPPLIER"),
    summary="New supplier for a shared excipient",
    product_strids={TABLET.strid, INJECTION.strid},
)

TABLET_FDA = Licence(
    strid=seed_strid("example_licence", "TABLET_FDA"),
    product_strid=TABLET.strid,
    regulator_strid=REGULATORS_BY_CODE[RegulatorCode.FDA].strid,
    market_strids={MARKETS_BY_CODE[MarketCode.US].strid},
)
# One centralised licence, three markets (AC1.4); with TABLET_FDA, four market rows (AC4.1).
TABLET_EC = Licence(
    strid=seed_strid("example_licence", "TABLET_EC"),
    product_strid=TABLET.strid,
    regulator_strid=REGULATORS_BY_CODE[RegulatorCode.EC_EMA].strid,
    market_strids={
        MARKETS_BY_CODE[MarketCode.DE].strid,
        MARKETS_BY_CODE[MarketCode.FR].strid,
        MARKETS_BY_CODE[MarketCode.NO].strid,
    },
)
TABLET_ANVISA = Licence(
    strid=seed_strid("example_licence", "TABLET_ANVISA"),
    product_strid=TABLET.strid,
    regulator_strid=REGULATORS_BY_CODE[RegulatorCode.ANVISA].strid,
    market_strids={MARKETS_BY_CODE[MarketCode.BR].strid},
)
# Cambodia: rule set unknown (AC2.5).
TABLET_DDF = Licence(
    strid=seed_strid("example_licence", "TABLET_DDF"),
    product_strid=TABLET.strid,
    regulator_strid=REGULATORS_BY_CODE[RegulatorCode.KH_DDF].strid,
    market_strids={MARKETS_BY_CODE[MarketCode.KH].strid},
)
TABLET_SWISSMEDIC = Licence(
    strid=seed_strid("example_licence", "TABLET_SWISSMEDIC"),
    product_strid=TABLET.strid,
    regulator_strid=REGULATORS_BY_CODE[RegulatorCode.SWISSMEDIC].strid,
    market_strids={MARKETS_BY_CODE[MarketCode.CH].strid},
)
# A biologic: 21 CFR 601.12, not 314.70.
INJECTION_FDA = Licence(
    strid=seed_strid("example_licence", "INJECTION_FDA"),
    product_strid=INJECTION.strid,
    regulator_strid=REGULATORS_BY_CODE[RegulatorCode.FDA].strid,
    market_strids={MARKETS_BY_CODE[MarketCode.US].strid},
)
# Same market as TABLET_ANVISA, different rule set: RDC 913/2024, not RDC 73/2016 (AC2.2).
INJECTION_ANVISA = Licence(
    strid=seed_strid("example_licence", "INJECTION_ANVISA"),
    product_strid=INJECTION.strid,
    regulator_strid=REGULATORS_BY_CODE[RegulatorCode.ANVISA].strid,
    market_strids={MARKETS_BY_CODE[MarketCode.BR].strid},
)

LICENCES: tuple[Licence, ...] = (
    TABLET_FDA,
    TABLET_EC,
    TABLET_ANVISA,
    TABLET_DDF,
    TABLET_SWISSMEDIC,
    INJECTION_FDA,
    INJECTION_ANVISA,
)

# No row for INJECTION_FDA: it shows as not yet classified, and the change isn't complete (AC4.3, AC7.2).
CLASSIFICATIONS: tuple[Classification, ...] = (
    Classification(
        strid=seed_strid("example_classification", "TABLET_FDA"),
        change_strid=CHANGE.strid,
        licence_strid=TABLET_FDA.strid,
        reporting_category_strid=REPORTING_CATEGORIES_BY_CODE[ReportingCategoryCode.US_CBE_30].strid,
        reasoning="Excipient supplier change with moderate potential to affect quality.",
    ),
    # One classification for Germany, France and Norway together (AC5.4).
    Classification(
        strid=seed_strid("example_classification", "TABLET_EC"),
        change_strid=CHANGE.strid,
        licence_strid=TABLET_EC.strid,
        reporting_category_strid=REPORTING_CATEGORIES_BY_CODE[ReportingCategoryCode.EU_IB].strid,
        reasoning="Not listed as IA or II in Guideline C/2025/5045, so IB by default.",
    ),
    Classification(
        strid=seed_strid("example_classification", "TABLET_ANVISA"),
        change_strid=CHANGE.strid,
        licence_strid=TABLET_ANVISA.strid,
        reporting_category_strid=REPORTING_CATEGORIES_BY_CODE[ReportingCategoryCode.BR_SYN_PA].strid,
        reasoning="RDC 73/2016 requires prior approval for this excipient change.",
    ),
    # Rule set unknown: a filing route with no category (AC6.2), shown as such (AC6.3).
    Classification(
        strid=seed_strid("example_classification", "TABLET_DDF"),
        change_strid=CHANGE.strid,
        licence_strid=TABLET_DDF.strid,
        filing_route=FilingRoute.PRIOR_APPROVAL,
        reasoning="No confirmed category list; DDF affiliate advises prior approval for supplier changes.",
    ),
    # Not affected is not a no-filing category (AC6.4).
    Classification(
        strid=seed_strid("example_classification", "TABLET_SWISSMEDIC"),
        change_strid=CHANGE.strid,
        licence_strid=TABLET_SWISSMEDIC.strid,
        reasoning="The Swiss licence registers a different excipient supplier, which is unchanged.",
    ),
    Classification(
        strid=seed_strid("example_classification", "INJECTION_ANVISA"),
        change_strid=CHANGE.strid,
        licence_strid=INJECTION_ANVISA.strid,
        reporting_category_strid=REPORTING_CATEGORIES_BY_CODE[ReportingCategoryCode.BR_BIO_MOD].strid,
        reasoning="Moderate quality change under RDC 913/2024.",
    ),
)
