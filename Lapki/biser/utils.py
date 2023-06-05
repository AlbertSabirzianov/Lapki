from biser.models import Jewelry

DATA_CATEGORY = {
        1: 'Кольца',
        2: 'Ожерелья',
        3: 'Серьги',
        4: 'Брелки',
        5: 'Браслеты',
    }

MASTER_EMAIL = 'Albertuno@mail.ru'


def get_order_mail(serializer):
    print(serializer.data)
    jewelry = Jewelry.objects.get(pk=serializer.data['jewelry'])
    name = serializer.data['name']
    text = f'Оформлен заказ от {name} /n' \
           f'Изделие: {jewelry.name}' 
           # Добавить ссылку на изделие)
    return text

