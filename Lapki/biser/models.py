from django.db import models


class Jewelry(models.Model):
    """Модель украшения."""

    name = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    icon = models.ImageField(
        upload_to='icons',
        verbose_name='Иконка'
    )
    make_time = models.DateTimeField(
        auto_created=True,
        auto_now=True,
        verbose_name='Время появления на сайте',
    )
    description = models.TextField(verbose_name='Подробное описание')
    price = models.FloatField(verbose_name='Цена в рублях')
    second_name = models.CharField(
        max_length=256,
        verbose_name='Короткое описание',
    )

    class Category(models.IntegerChoices):
        RING = 1, 'Кольца'
        NECK = 2, 'Ожерелья'
        EAR = 3, 'Серьги'
        KEYCHAIN = 4, 'Брелки'
        BRA = 5, 'Браслеты'

    category = models.PositiveSmallIntegerField(
        choices=Category.choices,
        verbose_name='Категория',
    )

    def __str__(self):
        return f'{self.name} ({self.second_name})'

    class Meta:
        ordering = ['-make_time']
        verbose_name = 'Украшение'
        verbose_name_plural = 'Украшения'


class Picture(models.Model):
    """Класс картинок украшения."""

    picture = models.ImageField(
        upload_to='pictures',
        verbose_name='Картинка',
    )
    jewelry = models.ForeignKey(
        Jewelry,
        on_delete=models.CASCADE,
        verbose_name='Украшение',
    )

    def __str__(self) -> str:
        return 'Картинка от украшения ' + self.jewelry.name

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Order(models.Model):
    """Модель заказа."""

    name = models.CharField(
        max_length=100,
        verbose_name='Имя заказчика',
    )
    make_time = models.DateTimeField(
        auto_now=True,
        verbose_name='Время заказа',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Коментарий к заказу'
    )
    jewelry = models.ManyToManyField(
        Jewelry,
        verbose_name='Украшения',
        related_name='all_jewelry',
    )
    mail = models.EmailField(
        verbose_name='Email'
    )
    phone_number = models.CharField(
        max_length=17,
        verbose_name='Телефон',
    )
    is_finished = models.BooleanField(
        default=False,
        verbose_name='Закончен ли заказ'
    )
    summ = models.FloatField(
        verbose_name='Сумма заказа',
        default=0,
    )

    def __str__(self) -> str:
        return 'Заказ ' + str(self.name) + ' ' + str(self.make_time)

    class Meta:
        ordering = ['-make_time']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
