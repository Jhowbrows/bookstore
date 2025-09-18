import pytest

from product.models import Product


@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Titulo teste do produto",
        description="Descrição do teste 1",
        price=999
    )

    assert product.title == "Titulo teste do produto"
    assert product.description == "Descrição do teste 1"
    assert product.price == 999
    assert product.id is not None
