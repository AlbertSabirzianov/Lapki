import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Jewelry, Picture, Order
from .utils import DATA_CATEGORY


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class JewelryGetSerializer(serializers.ModelSerializer):
    cat = serializers.SerializerMethodField()

    class Meta:
        model = Jewelry
        fields = (
            'pk',
            'name',
            'description',
            'second_name',
            'price',
            'cat',
            'icon'
        )

    def get_cat(self, obj):
        return DATA_CATEGORY[obj.category]


class JewelryPostSerializer(serializers.ModelSerializer):
    icon = Base64ImageField(
        required=False,
        allow_null=False
    )

    class Meta:
        model = Jewelry
        fields = (
            'name',
            'description',
            'price',
            'category',
            'icon',
            'second_name'
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Jewelry.objects.all(),
                fields=['name', 'second_name']
            )
        ]


class PictureSerializer(serializers.ModelSerializer):
    picture = Base64ImageField(
        required=False,
        allow_null=False
    )

    class Meta:
        model = Picture
        fields = (
            'pk',
            'picture',
            'jewelry'
        )
        read_only_fields = (
            'pk',
            'jewelry',
        )


class OrderGetSerializer(serializers.ModelSerializer):
    jewelry = JewelryGetSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Order
        fields = (
            'pk',
            'name',
            'make_time',
            'description',
            'jewelry',
            'mail',
            'phone_number'
        )
        read_only_fields = (
            'pk',
            'make_time'
        )


class OrderPostSerializer(serializers.ModelSerializer):
    jewelry = serializers.PrimaryKeyRelatedField(
        queryset=Jewelry.objects.all(),
        many=True,
    )

    class Meta:
        model = Order
        fields = (
            'name',
            'description',
            'summ',
            'jewelry',
            'mail',
            'phone_number'
        )

    def validate_summ(self, value):
        """Сумма должна быть больше нуля."""

        if value <= 0:
            raise serializers.ValidationError(
                'Сумма должна быть больше нуля.'
            )

        return value

    def validate_jewelry(self, value):
        """Заказ должен содержать украшения."""

        if not value:
            raise serializers.ValidationError(
                'Заказ должен содержать украшения'
            )

        return value
