import pytest

from product.models.category import Category
from product.serializers import ProductSerializer
from product.models import product


@pytest.mark.django_db
def test_product_serializer():
    

    category = Category.objects.create(title='Ficção Científica', slug='ficcao-cientifica')

    data = {
        "title": "Teste serializer",
        "description": "Testando o serializer",
        "price": 999.00,
        "category": [category.id]
    }

    
    serializer = ProductSerializer(data=data)

    
    assert serializer.is_valid(), f"Erros: {serializer.errors}"

    
    product = serializer.save()

    
    assert product.title == data["title"]  
    assert product.description == data["description"]  
    assert product.price == data["price"]  
    assert list(product.category.values_list('id', flat=True)) == data['category']

    
    serializer = ProductSerializer(product)
    serialized_data = serializer.data

    
    assert serialized_data["title"] == data["title"]
    assert serialized_data["description"] == data["description"]
    assert serialized_data["price"] == data["price"]
    assert serialized_data["id"] == product.id
    assert serialized_data["category"] == [category.id]