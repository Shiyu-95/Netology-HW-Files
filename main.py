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


def join_files(*files):
    with open(files[0]) as f:
        file1_name = f.name
        file1_content = f.read()
        lines1 = file1_content.count('\n')

    with open(files[1], encoding='UTF-8') as f:
        file2_name = f.name
        file2_content = f.read()
        lines2 = file2_content.count('\n')

    with open(files[2], encoding='UTF-8') as f:
        file3_name = f.name
        file3_content = f.read()
        lines3 = file3_content.count('\n')

    shortest = min(lines1, lines2, lines3)
    biggest = max(lines1, lines2, lines3)

    with open("recipes/file_for_join.txt", 'w') as f:
        if lines1 == shortest and lines2 == biggest:
            f.write(f'{file1_name}\n')
            f.write(f'{str(lines1)}\n')
            f.write(f'{file1_content}\n')
            f.write(f'{file3_name}\n')
            f.write(f'{str(lines3)}\n')
            f.write(f'{file3_content}\n')
            f.write(f'{file2_name}\n')
            f.write(f'{str(lines2)}\n')
            f.write(f'{file2_content}\n')
        elif lines2 == shortest and lines3 == biggest:
            f.write(f'{file2_name}\n')
            f.write(f'{str(lines2)}\n')
            f.write(f'{file2_content}\n')
            f.write(f'{file1_name}\n')
            f.write(f'{str(lines1)}\n')
            f.write(f'{file1_content}\n')
            f.write(f'{file3_name}\n')
            f.write(f'{str(lines3)}\n')
            f.write(f'{file3_content}\n')
        else:
            f.write(f'{file3_name}\n')
            f.write(f'{str(lines3)}\n')
            f.write(f'{file3_content}\n')
            f.write(f'{file2_name}\n')
            f.write(f'{str(lines2)}\n')
            f.write(f'{file2_content}\n')
            f.write(f'{file1_name}\n')
            f.write(f'{str(lines1)}\n')
            f.write(f'{file1_content}\n')


get_ingredients("recipes/Recipe.txt")
get_shop_list_by_dishes(['Омлет', "Запеченный картофель", "Фахитос"], 3)
join_files("recipes/Recipe.txt", "recipes/new_recipes.txt", "recipes/new_new_recipes.txt")
