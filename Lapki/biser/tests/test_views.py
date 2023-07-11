from http import HTTPStatus

from .test_setup import SetUpTestCase
from biser.models import Order, Jewelry, Picture


class OrderViewSetTestCase(SetUpTestCase):
    """Проверка обработки заказов."""

    def test_order_get(self):
        """Get запрос к заказам."""

        response = self.client.get(
            '/order/'
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            msg='get запрос прошёл неудачно'
        )

        self.assertEqual(
            len(response.data),
            1,
            msg='Нет заказов'
        )

        self.assertEqual(
            response.data[0]['name'],
            'Al'
        )

    def test_order_post(self):
        """Проверка отправки заказа."""

        response = self.client.post(
            '/order/',
            self.data_order_post,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.CREATED,
            msg='Не создался заказ'
        )

        self.assertTrue(
            Order.objects.filter(name='Albert').exists()
        )

        self.assertEqual(
            Order.objects.all().count(),
            2,
            msg='Не создался заказ'
        )


class JewelryViewSetTestCase(SetUpTestCase):
    """Проверка обработки украшений."""

    def test_post_jewelry(self):
        """Отправка украшения."""

        response = self.admin_client.post(
            '/jewelry/',
            self.data_post_jewelry,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.CREATED
        )
        self.assertTrue(
            Jewelry.objects.filter(name='lover').exists()
        )
        self.assertEqual(
            Jewelry.objects.all().count(),
            3
        )

    def test_get_all_jewelry(self):
        """Получение всех украшений."""

        response = self.client.get(
            '/jewelry/',
            format='json'
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.OK
        )

        self.assertEqual(
            len(response.data),
            2
        )

    def test_get_not_exists_jewelry(self):
        """Получение несуществующего украшения."""

        response = self.client.get(
            '/jewelry/33/',
            format='json'
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.NOT_FOUND
        )

    def test_filter_jewelry(self):
        """Проверка фильтра украшений."""

        response = self.client.get(
            '/jewelry/?category=1',
            format='json',
        )
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK
        )

        self.assertEqual(
            len(response.data),
            1
        )

        response = self.client.get(
            '/jewelry/?category=3',
            format='json'
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.OK
        )

        self.assertEqual(
            len(response.data),
            0
        )


class PictureViewSetTestCase(SetUpTestCase):
    """
    Проверка обработки картинок.
    """

    def test_get_pictures(self):
        """Проверка get запроса к картинкам."""

        res = self.client.get(
            '/jewelry/1/picture/',
            format='json'
        )

        self.assertEqual(
            res.status_code,
            HTTPStatus.OK
        )
        self.assertEqual(
            len(res.data),
            1
        )

    def test_get_not_exists_jewelry_pictures(self):
        """get запрос к картинкам несуществующего украшения."""

        res = self.client.get(
            '/jewelry/33/picture/',
            format='json'
        )

        self.assertEqual(
            res.status_code,
            HTTPStatus.NOT_FOUND
        )

    def test_post_picture(self):
        """Отправка картинки."""

        response = self.admin_client.post(
            '/jewelry/1/picture/',
            self.data_post_picture,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.CREATED
        )
        self.assertFalse(
            Picture.objects.filter(jewelry=self.jewelry_two).exists()
        )
        self.assertEqual(
            Picture.objects.filter(jewelry=self.jewelry_one).count(),
            2
        )

    def test_post_not_exists_jewelry_pictures(self):
        """Отправка картинки несуществующего украшения."""

        res = self.admin_client.post(
            '/jewelry/33/picture/',
            self.data_post_picture,
            format='json'
        )

        self.assertEqual(
            res.status_code,
            HTTPStatus.NOT_FOUND
        )
