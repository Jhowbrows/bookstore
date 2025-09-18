import pytest

from product.models.category import Category
from product.models import Product
from product.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_serializer():
    
    category = Category.objects.create(title='Terror', slug='terror')
    product = Product.objects.create(title='Drácula', price=45, active=True)
    product.category.add(category)

    
    serializer = ProductSerializer(instance=product)

   
    expected_data = {
        'title': 'Drácula',
        'description': None, 
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
    
    
    assert serializer.data['title'] == expected_data['title']
    assert serializer.data['price'] == expected_data['price']
    assert serializer.data['active'] == expected_data['active']
    assert serializer.data['category'][0]['title'] == expected_data['category'][0]['title']
