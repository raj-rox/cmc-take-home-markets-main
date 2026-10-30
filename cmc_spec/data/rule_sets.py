"""The seeded rule sets. Rows written out in full; strids derived from the code.

A market and product type no row covers has no rule set recorded ("rule set unknown"):
Brunei, Cambodia, Lao PDR, Myanmar, Thailand and Timor-Leste; and biologics in Argentina and the
ASEAN members.
"""

from __future__ import annotations

from cmc_spec.core import seed_strid
from cmc_spec.data.markets import MARKETS_BY_CODE
from cmc_spec.data.product_types import PRODUCT_TYPES_BY_CODE
from cmc_spec.models.market import MarketCode
from cmc_spec.models.product_type import ProductTypeCode
from cmc_spec.models.rule_set import RuleSet, RuleSetCode

RULE_SETS: tuple[RuleSet, ...] = (
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.US_CFR_314_70),
        code=RuleSetCode.US_CFR_314_70,
        name="US changes to an approved NDA or ANDA",
        source="21 CFR 314.70; FDA guidance 'Changes to an Approved NDA or ANDA' (2004)",
        market_strids={MARKETS_BY_CODE[MarketCode.US].strid},
        product_type_strids={PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid},
    ),
    # Biologics run a parallel scheme with the same tiers (E2): a separate rule set, so a biologic
    # never gets the drug categories.
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.US_CFR_601_12),
        code=RuleSetCode.US_CFR_601_12,
        name="US changes to an approved BLA",
        source=(
            "21 CFR 601.12; FDA guidance 'Chemistry, Manufacturing, and Controls Changes to an "
            "Approved Application: Certain Biological Products' (2021)"
        ),
        market_strids={MARKETS_BY_CODE[MarketCode.US].strid},
        product_type_strids={PRODUCT_TYPES_BY_CODE[ProductTypeCode.BIOLOGICAL].strid},
    ),
    # One rule set on every route to a licence: centralised, mutual recognition, decentralised, national (E5).
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.EU_VARIATIONS),
        code=RuleSetCode.EU_VARIATIONS,
        name="EU variations framework",
        source=(
            "Commission Regulation (EC) No 1234/2008 as amended by Delegated Regulation (EU) 2024/1701; "
            "classification Guideline C/2025/5045 (applicable 15 January 2026)"
        ),
        market_strids={
            MARKETS_BY_CODE[MarketCode.DE].strid,
            MARKETS_BY_CODE[MarketCode.FR].strid,
            MARKETS_BY_CODE[MarketCode.NO].strid,
        },
        product_type_strids={
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid,
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.BIOLOGICAL].strid,
        },
    ),
    # UK, Switzerland, Saudi Arabia and South Africa: the evidence describes one guideline each,
    # not separate rules for biologics, so each covers both product types.
    # Retains the pre-2024 EU rules: not bound by Regulation (EU) 2024/1701 (E2).
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.UK_VARIATIONS),
        code=RuleSetCode.UK_VARIATIONS,
        name="UK variations regime",
        source=(
            "Human Medicines Regulations 2012 (SI 2012/1916), regulation 65C and Schedule 10A; "
            "EU classification guideline 2013/C 223/01, pending revised MHRA guidance"
        ),
        market_strids={MARKETS_BY_CODE[MarketCode.GB].strid},
        product_type_strids={
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid,
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.BIOLOGICAL].strid,
        },
    ),
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.CH_VARIATIONS),
        code=RuleSetCode.CH_VARIATIONS,
        name="Swiss variations regime",
        source=(
            "Therapeutic Products Act and Ordinance on Medicinal Products; "
            "Swissmedic guidance ZL300 (updated February 2026)"
        ),
        market_strids={MARKETS_BY_CODE[MarketCode.CH].strid},
        product_type_strids={
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid,
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.BIOLOGICAL].strid,
        },
    ),
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.SA_VARIATIONS),
        code=RuleSetCode.SA_VARIATIONS,
        name="Saudi variations regime",
        source=(
            "SFDA Guidelines for Variation Requirements v6.3 (March 2025), aligned to the GCC guidelines"
        ),
        market_strids={MARKETS_BY_CODE[MarketCode.SA].strid},
        product_type_strids={
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid,
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.BIOLOGICAL].strid,
        },
    ),
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.ZA_VARIATIONS),
        code=RuleSetCode.ZA_VARIATIONS,
        name="South African variations regime",
        source=(
            "SAHPRA Guideline for Variations SAHPGL-HPA-06 v7/2025, "
            "with quality and clinical classification annexures"
        ),
        market_strids={MARKETS_BY_CODE[MarketCode.ZA].strid},
        product_type_strids={
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid,
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.BIOLOGICAL].strid,
        },
    ),
    # ASEAN: each member that publishes its own scheme gets its own rule set; none gets the AVG
    # itself (AC2.6). No rule set for Brunei, Cambodia, Lao PDR, Myanmar, Thailand or Timor-Leste.
    # Synthetic only: the AVG excludes biologics and the evidence doesn't show these schemes
    # covering them, so ASEAN biologics are "rule set unknown".
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.SG_HSA),
        code=RuleSetCode.SG_HSA,
        name="Singapore therapeutic product variations",
        source=(
            "HSA Guidance on Therapeutic Product Registration in Singapore, Appendices 13-14 "
            "(edition not in the evidence; to confirm)"
        ),
        market_strids={MARKETS_BY_CODE[MarketCode.SG].strid},
        product_type_strids={PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid},
    ),
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.MY_MVG),
        code=RuleSetCode.MY_MVG,
        name="Malaysian Variation Guideline",
        source="Malaysian Variation Guideline for Pharmaceutical Products, 2nd Edition (July 2022), based on AVG Revision 2",
        market_strids={MARKETS_BY_CODE[MarketCode.MY].strid},
        product_type_strids={PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid},
    ),
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.PH_PVG),
        code=RuleSetCode.PH_PVG,
        name="Philippine Variation Guidelines",
        source="Philippine Variation Guidelines V1.0 (22 April 2020)",
        market_strids={MARKETS_BY_CODE[MarketCode.PH].strid},
        product_type_strids={PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid},
    ),
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.ID_BPOM),
        code=RuleSetCode.ID_BPOM,
        name="Indonesian drug variation registration",
        source="PerBPOM 24/2017, as amended by PerBPOM 15/2023 and PerBPOM 23/2025",
        market_strids={MARKETS_BY_CODE[MarketCode.ID].strid},
        product_type_strids={PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid},
    ),
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.VN_DAV),
        code=RuleSetCode.VN_DAV,
        name="Vietnamese marketing authorisation variations",
        source="Circular 12/2025/TT-BYT, Appendix II",
        market_strids={MARKETS_BY_CODE[MarketCode.VN].strid},
        product_type_strids={PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid},
    ),
    # China: one scheme for both product types (E2).
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.CN_POST_APPROVAL),
        code=RuleSetCode.CN_POST_APPROVAL,
        name="Chinese post-approval changes",
        source=(
            "Provisions for Drug Registration (Order No. 27, 2020); "
            "Measures for the Administration of Post-Approval Changes of Drugs (Trial), "
            "NMPA Announcement No. 8 of 2021"
        ),
        market_strids={MARKETS_BY_CODE[MarketCode.CN].strid},
        product_type_strids={
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid,
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.BIOLOGICAL].strid,
        },
    ),
    # Brazil: separate rule sets by product type (E2).
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.BR_RDC_73_2016),
        code=RuleSetCode.BR_RDC_73_2016,
        name="Brazilian post-approval changes, synthetic and semi-synthetic",
        source="ANVISA RDC 73/2016",
        market_strids={MARKETS_BY_CODE[MarketCode.BR].strid},
        product_type_strids={PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid},
    ),
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.BR_RDC_913_2024),
        code=RuleSetCode.BR_RDC_913_2024,
        name="Brazilian post-approval changes, biological",
        source="ANVISA RDC 913/2024 (revoked RDC 413/2020)",
        market_strids={MARKETS_BY_CODE[MarketCode.BR].strid},
        product_type_strids={PRODUCT_TYPES_BY_CODE[ProductTypeCode.BIOLOGICAL].strid},
    ),
    # Mexico: both product types. Biologics carry additional administrativa / tecnica / cesion de
    # derechos subcategories on top of these tiers (E2); not seeded, see MEMO.
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.MX_MCRS),
        code=RuleSetCode.MX_MCRS,
        name="Mexican modifications to registration conditions",
        source="Reglamento de Insumos para la Salud; MCRS acuerdos 2022-2023 (menor/moderada/mayor since 28 August 2023)",
        market_strids={MARKETS_BY_CODE[MarketCode.MX].strid},
        product_type_strids={
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid,
            PRODUCT_TYPES_BY_CODE[ProductTypeCode.BIOLOGICAL].strid,
        },
    ),
    # Argentina: synthetic only. Biologics moved to Disp. 4351/2026, whose categories aren't seeded.
    RuleSet(
        strid=seed_strid("rule_set", RuleSetCode.AR_REM),
        code=RuleSetCode.AR_REM,
        name="Argentine post-registration modifications",
        source="Decreto 150/92; ANMAT Disposicion 5755/1996 and amendments",
        market_strids={MARKETS_BY_CODE[MarketCode.AR].strid},
        product_type_strids={PRODUCT_TYPES_BY_CODE[ProductTypeCode.SYNTHETIC].strid},
    ),
)

RULE_SETS_BY_CODE = {row.code: row for row in RULE_SETS}
