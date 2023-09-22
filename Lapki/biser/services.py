DATA_CATEGORY = {
        1: 'Кольца',
        2: 'Ожерелья',
        3: 'Серьги',
        4: 'Брелки',
        5: 'Браслеты',
    }

def get_text_mail(serializer):
    name = serializer.data['name']
    phone = serializer.data['phone_number']
    comment = serializer.data['description']
    summ = serializer.data['summ']
    text = f'Оформлен заказ от {name} \n' \
           f'На сумму {summ} \n' \
           f'Телефон: {phone} \n' \
           f'Коментарий к заказу: {comment}'
    return text
