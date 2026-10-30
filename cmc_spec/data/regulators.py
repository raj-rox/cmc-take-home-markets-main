"""The seeded regulators. Rows written out in full; strids derived from the code."""

from __future__ import annotations

from cmc_spec.core import seed_strid
from cmc_spec.data.markets import MARKETS_BY_CODE
from cmc_spec.models.market import MarketCode
from cmc_spec.models.regulator import Regulator, RegulatorCode

REGULATORS: tuple[Regulator, ...] = (
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.FDA),
        code=RegulatorCode.FDA,
        name="U.S. Food and Drug Administration (FDA)",
        market_strids={MARKETS_BY_CODE[MarketCode.US].strid},
    ),
    # Grants centralised licences on EMA's opinion; one licence covers every EU and EEA market (E5).
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.EC_EMA),
        code=RegulatorCode.EC_EMA,
        name="European Commission (centralised procedure, on EMA's opinion)",
        market_strids={
            MARKETS_BY_CODE[MarketCode.DE].strid,
            MARKETS_BY_CODE[MarketCode.FR].strid,
            MARKETS_BY_CODE[MarketCode.NO].strid,
        },
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.BFARM),
        code=RegulatorCode.BFARM,
        name="Federal Institute for Drugs and Medical Devices (BfArM)",
        market_strids={MARKETS_BY_CODE[MarketCode.DE].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.ANSM),
        code=RegulatorCode.ANSM,
        name="National Agency for the Safety of Medicines and Health Products (ANSM)",
        market_strids={MARKETS_BY_CODE[MarketCode.FR].strid},
    ),
    # E2 names only a "national competent authority"; the name is from public sources.
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.NOMA),
        code=RegulatorCode.NOMA,
        name="Norwegian Medical Products Agency (NOMA)",
        market_strids={MARKETS_BY_CODE[MarketCode.NO].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.MHRA),
        code=RegulatorCode.MHRA,
        name="Medicines and Healthcare products Regulatory Agency (MHRA)",
        market_strids={MARKETS_BY_CODE[MarketCode.GB].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.SWISSMEDIC),
        code=RegulatorCode.SWISSMEDIC,
        name="Swissmedic, Swiss Agency for Therapeutic Products",
        market_strids={MARKETS_BY_CODE[MarketCode.CH].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.SFDA),
        code=RegulatorCode.SFDA,
        name="Saudi Food and Drug Authority (SFDA)",
        market_strids={MARKETS_BY_CODE[MarketCode.SA].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.SAHPRA),
        code=RegulatorCode.SAHPRA,
        name="South African Health Products Regulatory Authority (SAHPRA)",
        market_strids={MARKETS_BY_CODE[MarketCode.ZA].strid},
    ),
    # ASEAN: every member has its own regulator. Nobody files with ASEAN itself (E4).
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.BDMCA),
        code=RegulatorCode.BDMCA,
        name="Brunei Darussalam Medicines Control Authority (BDMCA)",
        market_strids={MARKETS_BY_CODE[MarketCode.BN].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.KH_DDF),
        code=RegulatorCode.KH_DDF,
        name="Department of Drugs and Food (DDF), Ministry of Health, Cambodia",
        market_strids={MARKETS_BY_CODE[MarketCode.KH].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.BPOM),
        code=RegulatorCode.BPOM,
        name="Badan Pengawas Obat dan Makanan (BPOM)",
        market_strids={MARKETS_BY_CODE[MarketCode.ID].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.LA_FDD),
        code=RegulatorCode.LA_FDD,
        name="Food and Drug Department (FDD), Ministry of Health, Lao PDR",
        market_strids={MARKETS_BY_CODE[MarketCode.LA].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.NPRA),
        code=RegulatorCode.NPRA,
        name="National Pharmaceutical Regulatory Agency (NPRA)",
        market_strids={MARKETS_BY_CODE[MarketCode.MY].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.MM_DFDA),
        code=RegulatorCode.MM_DFDA,
        name="Department of Food and Drug Administration, Ministry of Health, Myanmar",
        market_strids={MARKETS_BY_CODE[MarketCode.MM].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.FDA_PH),
        code=RegulatorCode.FDA_PH,
        name="Food and Drug Administration Philippines (FDA Philippines)",
        market_strids={MARKETS_BY_CODE[MarketCode.PH].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.HSA),
        code=RegulatorCode.HSA,
        name="Health Sciences Authority (HSA)",
        market_strids={MARKETS_BY_CODE[MarketCode.SG].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.THAI_FDA),
        code=RegulatorCode.THAI_FDA,
        name="Thai Food and Drug Administration (Thai FDA)",
        market_strids={MARKETS_BY_CODE[MarketCode.TH].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.TL_DNFM),
        code=RegulatorCode.TL_DNFM,
        name="National Directorate of Pharmacy and Medicines (DNFM), Ministry of Health, Timor-Leste",
        market_strids={MARKETS_BY_CODE[MarketCode.TL].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.DAV),
        code=RegulatorCode.DAV,
        name="Drug Administration of Vietnam (DAV)",
        market_strids={MARKETS_BY_CODE[MarketCode.VN].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.NMPA),
        code=RegulatorCode.NMPA,
        name="National Medical Products Administration (NMPA)",
        market_strids={MARKETS_BY_CODE[MarketCode.CN].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.ANVISA),
        code=RegulatorCode.ANVISA,
        name="Agência Nacional de Vigilância Sanitária (ANVISA)",
        market_strids={MARKETS_BY_CODE[MarketCode.BR].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.COFEPRIS),
        code=RegulatorCode.COFEPRIS,
        name="Comisión Federal para la Protección contra Riesgos Sanitarios (COFEPRIS)",
        market_strids={MARKETS_BY_CODE[MarketCode.MX].strid},
    ),
    Regulator(
        strid=seed_strid("regulator", RegulatorCode.ANMAT),
        code=RegulatorCode.ANMAT,
        name="Administración Nacional de Medicamentos, Alimentos y Tecnología Médica (ANMAT)",
        market_strids={MARKETS_BY_CODE[MarketCode.AR].strid},
    ),
)

REGULATORS_BY_CODE = {row.code: row for row in REGULATORS}
