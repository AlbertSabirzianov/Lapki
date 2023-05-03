import base64

from django.core.files.base import ContentFile
from rest_framework import serializers

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
        fields = ('pk', 'name', 'description', 'price', 'cat', 'icon')

    def get_cat(self, obj):
        return DATA_CATEGORY[obj.category]


class JewelryPostSerializer(serializers.ModelSerializer):
    icon = Base64ImageField(required=False, allow_null=False)

    class Meta:
        model = Jewelry
        fields = ('name', 'description', 'price', 'category', 'icon')


class PictureSerializer(serializers.ModelSerializer):
    picture = Base64ImageField(required=False, allow_null=False)

    class Meta:
        model = Picture
        fields = ('pk', 'picture', 'jewelry')
        read_only_fields = ('jewelry', 'pk')


class OrderGetSerializer(serializers.ModelSerializer):
    jewelry = JewelryGetSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('pk', 'name', 'make_time', 'description',
                  'jewelry', 'mail', 'phone_number')
        read_only_fields = ('pk', 'make_time')


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('name', 'description',
                  'jewelry', 'mail', 'phone_number')
