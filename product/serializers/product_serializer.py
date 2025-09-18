from rest_framework import serializers

from product.models import Product
from product.models.category import Category
from .category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Product
        fields = '__all__'