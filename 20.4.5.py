import json
from collections import Counter

with open("asset-v1_SkillFactory+QAP-3.0+2021+type@asset+block@orders_july_2023.json", "r") as my_file:
    translator = json.load(my_file)
max_price = 0
max_quantity = 0
cnt_data = []
cnt_order = []
summ_1 = 0
summ_2 = 0
cnt = 0
user_totals = {}
max_order1 = ''
max_order2 = ""

for order_num, orders_data in translator.items():
    cnt += 1
    cnt_order.append(order_num)
    price = orders_data['price']
    quantity = orders_data['quantity']
    date = orders_data['date']
    user_id = orders_data['user_id']
    summ_1 += price
    summ_2 += quantity

    if price > max_price:
        max_order1 = order_num
        max_price = price

    if quantity > max_quantity:
        max_order2 = order_num
        max_quantity = quantity

    parts = date.split("-")
    year, month, day = parts
    cnt_data.append(int(day))

    day_counts = Counter(cnt_data)

    if day_counts:
        most_common_day, count = day_counts.most_common(1)[0]

    order_counts = Counter(cnt_order)

    if day_counts:
        most_order_counts, count = order_counts.most_common(1)[0]

    order_total = price

    if user_id not in user_totals:
        user_totals[user_id] = 0
    user_totals[user_id] += order_total

if user_totals:
    max_user = max(user_totals, key=user_totals.get)
    max_total = user_totals[max_user]

print(f'Номер заказа с самой большой стоимостью: {max_order1}, стоимость заказа: {max_price}')
print(f'Номер заказа с самым большим кол-вом товаров: {max_order2}, кол-во товаров: {max_quantity}')
print(f"Больше всего заказов в июле было {most_common_day}-го числа")
print(f"Больше всего заказов в июле было у пользователя {most_order_counts}")
print(f"Пользователь с ID {max_user} имеет самую большую суммарную стоимость заказов за июль")
print(f"Средняя стоимость заказа {summ_1 // cnt}")
print(f"Среднее кол-во товаров {summ_2 // cnt}")
