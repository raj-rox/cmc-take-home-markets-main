"""A product type: the kind of product a rule set is written for."""

from __future__ import annotations

from typing import Annotated

from cmc_spec.core import DataModel, Reference, ReferenceCode, Strid, reference_data


class ProductTypeCode(ReferenceCode):
    SYNTHETIC = "SYNTHETIC"
    BIOLOGICAL = "BIOLOGICAL"


@reference_data
class ProductType(DataModel):
    """A product type a rule set can apply to. Seeded in `data/product_types.py`."""

    code: ProductTypeCode
    name: str


ProductTypeRef = Annotated[Strid, Reference(ProductType)]
