import shutil
import tempfile

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from django.test import override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.authtoken.models import Token

from biser.models import Jewelry, Order, Picture
from .utils import IMAGE_64

TEMPLATE_MEDIA_DIR = tempfile.mkdtemp()
GIF = (
    b'\x47\x3B'
)


User = get_user_model()


@override_settings(MEDIA_ROOT=TEMPLATE_MEDIA_DIR)
class SetUpTestCase(APITestCase):
    """Класс API тестов."""

    IMAGE_64 = 'data:image/jpeg;base64,' + IMAGE_64

    data_verbose_order = {
        'name': 'Имя заказчика',
        'make_time': 'Время заказа',
        'description': 'Коментарий к заказу',
        'jewelry': 'Украшения',
        'mail': 'Email',
        'phone_number': 'Телефон',
        'is_finished': 'Закончен ли заказ',
        'summ': 'Сумма заказа',
    }

    data_verbose_jewelry = {
        'name': 'Название',
        'icon': 'Иконка',
        'make_time': 'Время появления на сайте',
        'description': 'Подробное описание',
        'price': 'Цена в рублях',
        'second_name': 'Короткое описание',
        'category': 'Категория',
    }

    data_verbose_picture = {
        'picture': 'Картинка',
        'jewelry': 'Украшение'
    }

    data_order_post = {
        'name': 'Albert',
        'description': 'test_description',
        'summ': 33,
        'jewelry': [1],
        'mail': 'test@mail.ru',
        'phone_number': '1234567',
    }

    data_post_jewelry = {
        'icon': IMAGE_64,
        'price': 200,
        'name': 'lover',
        'description': 'LOVE',
        'second_name': 'second love',
        'category': 3,
    }

    data_post_picture = {
        'picture': IMAGE_64,
    }

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.admin = User.objects.create(
            username='master',
            first_name='Master',
            email='master@mail.ru',
            is_staff=True,
        )
        cls.admin_client = APIClient()
        cls.icon = SimpleUploadedFile(
            name='icon.gif',
            content=GIF,
            content_type='image/gif'
        )
        cls.jewelry_one = Jewelry.objects.create(
            name='Jewelry_one',
            icon=cls.icon,
            description='test_description',
            price=33.0,
            second_name='test_second_name',
            category=1,
        )
        cls.jewelry_two = Jewelry.objects.create(
            name='Jewelry_two',
            icon=cls.icon,
            description='test_description',
            price=33.0,
            second_name='test_second_name',
            category=2,
        )
        cls.order = Order.objects.create(
            name='Al',
            description='test_description',
            mail='test@mail.ru',
            phone_number='1234567',
            summ=33,
        )
        cls.order.jewelry.set([cls.jewelry_one])
        cls.picture = Picture.objects.create(
            picture=cls.icon,
            jewelry=cls.jewelry_one,
        )

    def setUp(self) -> None:
        super(SetUpTestCase, self).setUp()
        self.admin_client.force_authenticate(
            self.admin,
            Token.objects.create(
                user=self.admin
            )
        )
        self.not_admin = APIClient()
        self.not_admin.force_authenticate(
            user=User.objects.create(
                username='not_admin',
                first_name='not_admin',
                email='not@mail.ru',
            ),
            token=Token.objects.create(
                user=User.objects.get(username='not_admin')
            )
        )

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(TEMPLATE_MEDIA_DIR, ignore_errors=True)
        super().tearDownClass()
