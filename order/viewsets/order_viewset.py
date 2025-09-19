from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from order.models import Order
from order.serializer import OrderSerializer


class OrderViewSet(ModelViewSet):
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]

    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")
