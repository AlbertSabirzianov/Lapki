from http import HTTPStatus

from .test_setup import SetUpTestCase


class SerializersTestCase(SetUpTestCase):
    """
    Проверка сериализаторов.
    """

    def test_post_order_with_zero_summ(self):
        """Отсылаем заказ равный нулю."""

        response = self.client.post(
            '/order/',
            {
                'name': 'Albert',
                'description': 'test_description',
                'summ': 0,
                'jewelry': [1],
                'mail': 'test@mail.ru',
                'phone_number': '1234567',
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.BAD_REQUEST,
        )

    def test_post_order_with_no_jewelry(self):
        """Отсылаем заказ без украшений."""

        response = self.client.post(
            '/order/',
            {
                'name': 'Albert',
                'description': 'test_description',
                'summ': 50,
                'jewelry': [],
                'mail': 'test@mail.ru',
                'phone_number': '1234567',
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.BAD_REQUEST,
        )

    def test_get_jewelry_serializer_cat(self):
        """Проверка отображения категории."""

        res = self.client.get(
            '/jewelry/1/',
            format='json',
        )

        self.assertEqual(
            res.data['cat'],
            'Кольца'
        )

    def test_post_jewelry_with_same_name_and_second_name(self):
        """
        Отправка украшения с уже существующим именем и коротким описанием.
        """

        response = self.admin_client.post(
            '/jewelry/',
            {
                'icon': self.IMAGE_64,
                'price': 200,
                'name': 'Jewelry_one',
                'description': 'LOVE',
                'second_name': 'test_second_name',
                'category': 3,
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.BAD_REQUEST
        )
