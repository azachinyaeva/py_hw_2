import codecs

with codecs.open('file.txt', encoding='utf-8') as fin:
    cook_book = {}
    cook_book_keys = ["ingredient_name", "quantity", "measure"]
    for line in fin:
        name = line.strip()
        num = int(fin.readline())
        ingredients = []
        for _ in range(num):
            ingr = fin.readline().strip().split("|")
            ing_dict = dict(zip(cook_book_keys, ingr))
            ingredients.append(ing_dict)
        fin.readline()
        cook_book[name] = ingredients


def show(cook_book):
    for dish, ingredients in cook_book.items():
        print(dish)
        for i in ingredients:
            print('  ', i['ingredient_name'].strip(), i['quantity'].strip(), i['measure'].strip())


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    shop_list_keys = ["measure", "quantity"]
    for dish_ in dishes:
        for i in cook_book[dish_]:
            ing_name = i["ingredient_name"]
            if ing_name in shop_list:
                shop_list[ing_name]["quantity"] += int(i["quantity"]) * person_count
            else:
                shop_list[ing_name] = {"quantity": int(i["quantity"]) * person_count, "measure": i["measure"]}
    return shop_list


show(cook_book)
print(get_shop_list_by_dishes(["Омлет", "Фахитос"], 3))
