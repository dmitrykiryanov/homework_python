def get_dict(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            key = line.strip()
            cook_book.setdefault(key)
            ingredient_qnt = int(file.readline().strip())
            ing_list = []
            for ingredient in range(ingredient_qnt):
                ing_dict = {}
                str = file.readline().strip()
                str_list = list(str.split("|"))
                ing_dict['ingredient_name'] = str_list[0]
                ing_dict['quantity'] = int(str_list[1])
                ing_dict['measure'] = str_list[2]
                ing_list.append(ing_dict)
            cook_book[key] = ing_list
            file.readline().strip()
    return cook_book
cook_book_new = get_dict('recipes.txt')

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish, recipe in cook_book_new.items():
        if dish in dishes:
            for ingredient in recipe:
                key = ingredient.pop('ingredient_name')
                if key not in shop_list_by_dishes:
                    shop_list_by_dishes.setdefault(key)
                    ingredient['quantity'] = person_count*ingredient['quantity']
                    shop_list_by_dishes[key] = ingredient
                else:
                    ingredient['quantity'] = ingredient['quantity'] + person_count * ingredient['quantity']
                    shop_list_by_dishes[key] = ingredient
        else:
            continue
    return shop_list_by_dishes
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



