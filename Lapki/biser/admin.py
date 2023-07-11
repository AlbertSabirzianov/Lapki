from django.contrib import admin

from .models import Jewelry, Picture, Order


class JewelryAdmin(admin.ModelAdmin):
    """
    Поиск по полям: имя, second name
    Фильтрация по: категории
    Быстро изменить: цену
    """

    list_display = ('name', 'second_name', 'price', 'category')
    list_display_links = ('name',)
    search_fields = ('name', 'second_name')
    search_help_text = 'поиск по названию'
    list_editable = ('price', 'second_name')
    list_filter = ('price', 'category')


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


class PictureAdmin(admin.ModelAdmin):

    list_display = ('jewelry', 'picture')
    list_display_links = ('jewelry',)
    search_fields = ('jewelry__name',)
    search_help_text = 'Поиск по названию украшения'
    list_editable = ('picture',)


admin.site.register(Jewelry, JewelryAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Order, OrderAdmin)
