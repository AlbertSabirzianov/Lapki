DATA_CATEGORY = {
        1: 'Кольца',
        2: 'Ожерелья',
        3: 'Серьги',
        4: 'Брелки',
        5: 'Браслеты',
    }

MASTER_EMAIL = 'Albertuno@mail.ru'


def get_order_mail(serializer):
    name = serializer.data['name']
    phone = serializer.data['phone_number']
    comment = serializer.data['description']
    summ = serializer.data['summ']
    text = f'Оформлен заказ от {name} \n' \
           f'На сумму {summ}' \
           f'Телефон: {phone} \n' \
           f'Коментарий к заказу: {comment}'
    return text
