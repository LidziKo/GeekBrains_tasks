items = []
count = 1  # будет хранить номер товара

while True:
    product_name = input('Введите название товара\n(Введите пустое название, чтобы выйти): ')
    if product_name == '':  # выход из цикла
        break

    product_price = input('Введите цену товара: ')
    if product_price.isdigit():  # проверка на введение чисел
        product_price = int(product_price)
    else:
        print('Введена некорректная цена')
        continue

    product_qty = input('Введите количество товара: ')
    if product_qty.isdigit():  # проверка на введение чисел
        product_qty = int(product_qty)
    else:
        print('Введено некорректное кол-во')
        continue

    product_measurement = input('Введите единицу измерения продукта: ')

    item = {
        'Название': product_name,
        'Цена': product_price,
        'Количество': product_qty,
        'Единицы': product_measurement
    }

    tpl = (count, item)  # создание кортежа
    items.append(tpl)
    count += 1

#  item_info - кортеж; хранится номер товара count и информация о нём item
for item_info in items:
    print(item_info)

analytics = {
    'Название': [],
    'Цена': [],
    'Количество': [],
    'Единицы': []
}

for item_info in items:  # for in, потому что индекс не нужен
    item_dict = item_info[1]  # item_info[1] - обращение к первому индексу кортежа
    # добавление к ключу одного словаря необходимых элементов из другого словаря
    analytics['Название'].append(item_dict['Название'])
    analytics['Цена'].append(item_dict['Цена'])
    analytics['Количество'].append(item_dict['Количество'])
    analytics['Единицы'].append(item_dict['Единицы'])

print(analytics)
