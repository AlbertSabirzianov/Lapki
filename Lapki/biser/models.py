from django.db import models


class Jewelry(models.Model):
    """Модель украшения."""
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons')
    make_time = models.DateTimeField(auto_created=True, auto_now=True)
    description = models.TextField()
    price = models.FloatField()

    class Category(models.IntegerChoices):
        RING = 1, 'Кольца'
        NECK = 2, 'Ожерелья'
        EAR = 3, 'Серьги'
        KEYCHAIN = 4, 'Брелки'
        BRA = 5, 'Браслеты'

    category = models.PositiveSmallIntegerField(choices=Category.choices)

    class Meta:
        ordering = ['-make_time']


class Picture(models.Model):
    """Класс картинок украшения."""
    picture = models.ImageField(upload_to='pictures')
    jewelry = models.ForeignKey(
        Jewelry,
        on_delete=models.CASCADE,
    )


class Order(models.Model):
    """Модель заказа."""
    name = models.CharField(max_length=100)
    make_time = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    mail = models.EmailField()
    phone_number = models.CharField(max_length=17)

    class Meta:
        ordering = ['-make_time']
