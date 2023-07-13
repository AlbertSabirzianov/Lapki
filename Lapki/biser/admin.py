from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Jewelry, Picture, Order


@admin.register(Jewelry)
class JewelryAdmin(admin.ModelAdmin):
    """
    Поиск по полям: имя, second name
    Фильтрация по: категории
    Быстро изменить: цену
    """

    list_display = ('name', 'show_icon', 'second_name', 'price', 'category')
    list_display_links = ('name',)
    search_fields = ('name', 'second_name')
    search_help_text = 'поиск по названию'
    list_editable = ('price', 'second_name')
    list_filter = ('price', 'category')

    def show_icon(self, obj):
        """
        Показываем картинку вместо ссылки на неё.
        """

        if obj.icon:
            return mark_safe("<img src='{}' width='80' />".format(obj.icon.url))
        return 'None'

    show_icon.__name__ = 'Иконка'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Поиск по полям: Имя заказчика, название украшения
    Фильтрация: по выполненным
    Быстро изменить: выполнен
    """

    filter_horizontal = ['jewelry']
    list_display = ('name', 'description', 'summ', 'is_finished')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_editable = ('is_finished',)
    list_filter = ('is_finished',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):

    list_display = ('jewelry', 'show_picture')
    list_display_links = ('jewelry', 'show_picture')
    search_fields = ('jewelry__name',)
    search_help_text = 'Поиск по названию украшения'

    def show_picture(self, obj):
        """
        Показываем саму картинку, а не ссылку на неё.
        """

        if obj.picture:
            return mark_safe("<img src='{}' width='60' />".format(obj.picture.url))
        return 'None'

    show_picture.__name__ = 'Картинка'
