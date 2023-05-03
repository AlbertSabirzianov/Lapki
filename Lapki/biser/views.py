from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Jewelry, Picture, Order
from .paginations import JewelryPaginator
from .serializers import JewelryGetSerializer, JewelryPostSerializer, PictureSerializer, OrderGetSerializer, \
    OrderPostSerializer
from .permissions import IsAdminOrReadOnly


class JewelryViewSet(ModelViewSet):
    queryset = Jewelry.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    pagination_class = JewelryPaginator

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return JewelryGetSerializer
        return JewelryPostSerializer


class PictureViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    serializer_class = PictureSerializer

    def get_jewelry(self):
        return get_object_or_404(Jewelry, pk=self.kwargs['jewelry_id'])

    def get_queryset(self):
        return Picture.objects.filter(jewelry=self.get_jewelry())

    def perform_create(self, serializer):
        serializer.save(jewelry=self.get_jewelry())


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderGetSerializer
        return OrderPostSerializer

    # Дописать функционал отправки письма Мастеру



