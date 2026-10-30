"""The seeded markets: the countries in scope. Rows written out in full; strids derived from the code."""

from __future__ import annotations

from cmc_spec.core import seed_strid
from cmc_spec.models.market import Market, MarketCode

MARKETS: tuple[Market, ...] = (
    Market(
        strid=seed_strid("market", MarketCode.US),
        code=MarketCode.US,
        name="United States",
    ),
    Market(
        strid=seed_strid("market", MarketCode.DE),
        code=MarketCode.DE,
        name="Germany",
    ),
    Market(
        strid=seed_strid("market", MarketCode.FR),
        code=MarketCode.FR,
        name="France",
    ),
    Market(
        strid=seed_strid("market", MarketCode.NO),
        code=MarketCode.NO,
        name="Norway",
    ),
    Market(
        strid=seed_strid("market", MarketCode.GB),
        code=MarketCode.GB,
        name="United Kingdom",
    ),
    Market(
        strid=seed_strid("market", MarketCode.CH),
        code=MarketCode.CH,
        name="Switzerland",
    ),
    Market(
        strid=seed_strid("market", MarketCode.SA),
        code=MarketCode.SA,
        name="Saudi Arabia",
    ),
    Market(
        strid=seed_strid("market", MarketCode.ZA),
        code=MarketCode.ZA,
        name="South Africa",
    ),
    Market(
        strid=seed_strid("market", MarketCode.CN),
        code=MarketCode.CN,
        name="China",
    ),
    Market(
        strid=seed_strid("market", MarketCode.BR),
        code=MarketCode.BR,
        name="Brazil",
    ),
    Market(
        strid=seed_strid("market", MarketCode.MX),
        code=MarketCode.MX,
        name="Mexico",
    ),
    Market(
        strid=seed_strid("market", MarketCode.AR),
        code=MarketCode.AR,
        name="Argentina",
    ),
    Market(
        strid=seed_strid("market", MarketCode.BN),
        code=MarketCode.BN,
        name="Brunei Darussalam",
    ),
    Market(
        strid=seed_strid("market", MarketCode.KH),
        code=MarketCode.KH,
        name="Cambodia",
    ),
    Market(
        strid=seed_strid("market", MarketCode.ID),
        code=MarketCode.ID,
        name="Indonesia",
    ),
    Market(
        strid=seed_strid("market", MarketCode.LA),
        code=MarketCode.LA,
        name="Lao PDR",
    ),
    Market(
        strid=seed_strid("market", MarketCode.MY),
        code=MarketCode.MY,
        name="Malaysia",
    ),
    Market(
        strid=seed_strid("market", MarketCode.MM),
        code=MarketCode.MM,
        name="Myanmar",
    ),
    Market(
        strid=seed_strid("market", MarketCode.PH),
        code=MarketCode.PH,
        name="Philippines",
    ),
    Market(
        strid=seed_strid("market", MarketCode.SG),
        code=MarketCode.SG,
        name="Singapore",
    ),
    Market(
        strid=seed_strid("market", MarketCode.TH),
        code=MarketCode.TH,
        name="Thailand",
    ),
    Market(
        strid=seed_strid("market", MarketCode.TL),
        code=MarketCode.TL,
        name="Timor-Leste",
    ),
    Market(
        strid=seed_strid("market", MarketCode.VN),
        code=MarketCode.VN,
        name="Viet Nam",
    ),
)

MARKETS_BY_CODE = {row.code: row for row in MARKETS}
