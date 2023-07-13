from http import HTTPStatus

from .test_setup import SetUpTestCase


class PermissionsTestCase(SetUpTestCase):
    """
    Проверка доступа к украшениям.
    """

    def test_post_jewelry_not_UNAUTHORIZED(self):
        """Отправка украшения не зарегестрированным пользователем."""

        res = self.client.post(
            '/jewelry/',
            self.data_post_jewelry,
            format='json'
        )

        self.assertEqual(
            res.status_code,
            HTTPStatus.UNAUTHORIZED
        )

    def test_post_picture_not_UNAUTHORIZED(self):
        """Отправка картинки не зарегестрированным пользователем."""

        res = self.client.post(
            '/jewelry/1/picture/',
            {},
            format='json'
        )

        self.assertEqual(
            res.status_code,
            HTTPStatus.UNAUTHORIZED
        )

    def test_post_jewelry_not_admin(self):
        """Отправка украшения не админом."""

        res = self.not_admin.post(
            '/jewelry/',
            self.data_post_jewelry,
            format='json'
        )

        self.assertEqual(
            res.status_code,
            HTTPStatus.FORBIDDEN
        )

    def test_post_picture_not_admin(self):
        """Отправка картинки не админом."""

        res = self.not_admin.post(
            '/jewelry/1/picture/',
            {},
            format='json'
        )

        self.assertEqual(
            res.status_code,
            HTTPStatus.FORBIDDEN
        )
