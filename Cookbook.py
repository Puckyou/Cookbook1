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


def get_shop_list_by_dishes(dishes, person_count):
    with open("book.txt", "r", encoding="utf8" ) as f:
        new_item_list = {}
        lines = f.readlines()
        ingridient_dict = {}
        shop_list = {}
        new_shop_list_item = {}
        new_shop_list = {}
        for dish in dishes:
            for num, line in enumerate(lines):
                if line.strip() == dish:
                    new_list = lines[num+2:num+int(lines[num+1])+2]
                    for item in new_list:
                        new_list = item.strip()
                        my_list = new_list.split(" | ")
                        new_shop_list['ingridient_name'] = my_list[0]
                        new_shop_list['quantity'] = int(my_list[1])
                        new_shop_list['measure'] = my_list[2]
                        new_shop_list['quantity'] *= person_count
                        if new_shop_list['ingridient_name'] not in shop_list:
                            shop_list[new_shop_list['ingridient_name']] = dict(new_shop_list)
                        else:
                            shop_list[new_shop_list['ingridient_name']]['quantity'] += new_shop_list['quantity']
    return shop_list

def create_file():
    f = open("book.txt", "w", encoding="utf8")
    new_book = {}
    for dish,ingridient in cook_book.items():
        ingridient_list = []
        for i in ingridient:
            ingridient_list.append(list(i.values()))
        new_book[dish] = ingridient_list
    for dish, ingridient in new_book.items():
        f.write(dish +"\n" + str(len(ingridient)) +"\n")
        for i in ingridient:
            f.write(" | ".join(str(item) for item in i) + "\n")
    f.close()

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
