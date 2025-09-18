import pytest

from product.models.category import Category
from product.models import Product
from product.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_serializer():
    """
    Testa o serializer do Product (apenas serialização/leitura).
    """
    # 1. Preparação
    category = Category.objects.create(title='Terror', slug='terror')
    product = Product.objects.create(title='Drácula', price=45, active=True)
    product.category.add(category)

    # 2. Ação
    serializer = ProductSerializer(instance=product)

    # 3. Verificação
    # A categoria será um objeto aninhado por causa da sua definição no serializer
    expected_data = {
        'title': 'Drácula',
        'description': None, # O valor padrão é None/null
        'price': 45, # PositiveIntegerField arredonda para o inteiro mais próximo
        'active': True,
        'category': [
            {
                'title': 'Terror',
                'slug': 'terror',
                'description': None,
                'active': True
            }
        ]
    }
    
    # O DRF não garante a ordem dos campos, então comparamos item por item
    assert serializer.data['title'] == expected_data['title']
    assert serializer.data['price'] == expected_data['price']
    assert serializer.data['active'] == expected_data['active']
    assert serializer.data['category'][0]['title'] == expected_data['category'][0]['title']
