"""The seeded product types. Rows written out in full; strids derived from the code."""

from __future__ import annotations

from cmc_spec.core import seed_strid
from cmc_spec.models.product_type import ProductType, ProductTypeCode

PRODUCT_TYPES: tuple[ProductType, ...] = (
    ProductType(
        strid=seed_strid("product_type", ProductTypeCode.SYNTHETIC),
        code=ProductTypeCode.SYNTHETIC,
        name="Synthetic",
    ),
    ProductType(
        strid=seed_strid("product_type", ProductTypeCode.BIOLOGICAL),
        code=ProductTypeCode.BIOLOGICAL,
        name="Biological",
    ),
)

PRODUCT_TYPES_BY_CODE = {row.code: row for row in PRODUCT_TYPES}
