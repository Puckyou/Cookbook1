cook_book = {
  'яйчница': [
    {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
  'стейк': [
    {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
    {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
  'салат': [
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
    {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
  }

def get_the_dish(dishes):
    new_cook_book = {}
    with open("book.txt", "r", encoding="utf8" ) as f:
        cook_book = f.readlines()
        for dish in dishes:
            for i, line in enumerate(cook_book):
                if line.strip() == dish:
                    dish_list = []
                    dish_name = cook_book[i]
                    ingridient_count = int(cook_book[i + 1]) + i + 2
                    for n in range(i+2,ingridient_count):
                            new_list = cook_book[n].strip()
                            my_list = new_list.split(" | ")
                            new_ingridient = {}
                            new_ingridient['ingridient_name'] = my_list[0]
                            new_ingridient['quantity'] = int(my_list[1])
                            new_ingridient['measure'] = my_list[2]
                            dish_list.append(new_ingridient)
                            new_cook_book[dish] = dish_list
    return new_cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_the_dish(dishes)
    shop_list = {}
    for dish, ingridients in cook_book.items():
        for ingridient in ingridients:
          new_shop_list_item = dict(ingridient)
          new_shop_list_item['quantity'] *= person_count
          if new_shop_list_item['ingridient_name'] not in shop_list:
            shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
          else:
            shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def create_file():
    with open("book.txt", "w", encoding="utf8") as f:
        for dish, ingridient in cook_book.items():
            f.write("{}\n{}\n".format(dish, len(ingridient)))
            for i in ingridient:
                n = [i['ingridient_name'], i['quantity'], i['measure']]
                f.write("{}\n".format(" | ".join(str(item) for item in n)))

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))

def create_shop_list():
      create_file()
      person_count = int(input('Введите количество человек: '))
      dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
      shop_list = get_shop_list_by_dishes(dishes, person_count)
      print_shop_list(shop_list)
create_shop_list()
