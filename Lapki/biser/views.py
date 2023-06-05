from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from django_filters.rest_framework import DjangoFilterBackend

from django.core.mail import send_mail

from .models import Jewelry, Picture, Order
from .serializers import JewelryGetSerializer, JewelryPostSerializer, PictureSerializer, OrderGetSerializer, \
    OrderPostSerializer
from .permissions import IsAdminOrReadOnly
from .utils import get_order_mail


class JewelryViewSet(ModelViewSet):
    queryset = Jewelry.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category',)

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
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderGetSerializer
        return OrderPostSerializer

    def perform_create(self, serializer):
        serializer.save()
        send_mail(
            subject='Новый заказ!',
            message=get_order_mail(serializer),
            from_email='Albertuno@mail.ru',
            recipient_list=['natavalizer@gmail.com'],
            fail_silently=False
        )
        
    # Дописать функционал отправки письма Мастеру



