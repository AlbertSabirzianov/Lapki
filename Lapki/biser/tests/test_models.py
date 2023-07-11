from .test_setup import SetUpTestCase


class VerboseTestCase(SetUpTestCase):
    """Проверка verbose модели."""

    def test_order_verbose_name(self):
        """Проверка verbose модели заказа."""

        for field, text in self.data_verbose_order.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.order._meta.get_field(field).verbose_name,
                    text
                )

    def test_jewelry_verbose_name(self):
        """Проверка verbose модели украшения."""

        for field, text in self.data_verbose_jewelry.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.jewelry_one._meta.get_field(field).verbose_name,
                    text
                )

    def test_picture_verbose_name(self):
        """Проверка verbose модели картинки."""

        for field, text in self.data_verbose_picture.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.picture._meta.get_field(field).verbose_name,
                    text
                )


class StrTestCase(SetUpTestCase):
    """Проверка магического метода __str__."""

    def test_jewelry_str(self):
        """Строковое представление модели украшения."""

        self.assertEqual(
            str(self.jewelry_one),
            'Jewelry_one (test_second_name)',
            msg='Не работает метод __str__()'
        )

    def test_picture_str(self):
        """Строковое представление модели картинки."""

        self.assertEqual(
            str(self.picture),
            'Картинка от украшения Jewelry_one'
        )
