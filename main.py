import os


def get_ingredients(file):
    cook_book = {}
    ingr_inside = {}
    dish = None
    product_list = []
    with open(file) as f:
        for ind, line in enumerate(f):
            line = line.replace('\n', "")  # в строке обрезаются переносы
            if line == '':  # если строка это перенос, то пропускаем
                continue
            if type(line) == str and len(line) != 1:  # проверка на длину для пропуска строки с кол-вом ингред в блюде
                if "|" in line:  # для строки с ингредиентами
                    ing_line = line.split(' | ')
                    ingr_inside['ingredient_name'] = ing_line[0]
                    ingr_inside['quantity'] = ing_line[1]
                    ingr_inside['measure'] = ing_line[2]
                    product_list.append(ingr_inside.copy())
                    cook_book[dish] = product_list
                    continue
                cook_book[line] = None
                dish = line
                product_list = []

    return cook_book


def get_shop_list_by_dishes(dishes, person_count: int):
    products_dict_prod = {}
    products_dict_mes_quan = {}
    for dish in dishes:
        items_from_file = get_ingredients("recipes/Recipe.txt")[dish]
        for product in items_from_file:
            products_dict_mes_quan["measure"] = product["measure"]
            if product["ingredient_name"] in products_dict_prod:
                products_dict_mes_quan["quantity"] = (int(product["quantity"]))*person_count
                products_dict_mes_quan["quantity"] += products_dict_prod[product['ingredient_name']]['quantity']
            else:
                products_dict_mes_quan["quantity"] = (int(product["quantity"]))*person_count
            products_dict_prod[product["ingredient_name"]] = products_dict_mes_quan.copy()
    return products_dict_prod


def join_files(path):
    count_lines = {}
    for file in os.listdir(path):
        if file == 'file_for_join.txt':
            continue
        file_path = '{}{}'.format(path, file)
        with open(file_path) as f:
            content = f.readlines()
            count_lines[file] = len(content)
            count_lines = dict(sorted(count_lines.items(), key=lambda x: x[1]))
    for key, value in count_lines.items():
        with open(path+key) as f:
            content_in_cycle = f.readlines()
        with open("recipes/file_for_join.txt", 'a') as f:
            f.write(f'{key}\n')
            f.write(f'{str(value)}\n')
            f.write(''.join(content_in_cycle))
            f.write('\n')


get_ingredients("recipes/Recipe.txt")
get_shop_list_by_dishes(['Омлет', "Запеченный картофель", "Фахитос"], 3)
join_files("recipes/")
