from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'colbasa': {
        'фарш, кг': 5,
        'специи, г': 10,
        'консерванты, л': 0.25,
    },
}


def recipe(request, recipe_name):
    try:
        servings = float(request.GET.get('servings'))
    except Exception:
        servings = 1

    recipe_items = DATA[recipe_name].copy() if DATA.get(recipe_name) else None

    if servings > 0 and recipe_items is not None:
        for item, quantity in recipe_items.items():
            recipe_items[item] = round(quantity * servings, 2)

    context = {
        'recipe': recipe_items
    }
    return render(request, 'calculator/index.html', context)
