import pytest
from product.models import Category, Product
from product.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_model():

    category = Category.objects.create(title='Aventura', slug='aventura')
    product = Product.objects.create(title='A ilha do Tesouro', price=29.90)
    product.category.add(category)

    assert product.title == 'A ilha do Tesouro'
    assert product.category.count() == 1
    assert product.category.first().title == 'Aventura'
    assert str(product) == 'A ilha do Tesouro'
