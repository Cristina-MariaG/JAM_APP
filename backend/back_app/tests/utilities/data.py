product_1 = {
    "product": {
        "id": 1,
        "flavor": {"id": 1, "flavor": "vanilla"},
        "type_contenant": {"id": 1, "type_contenant": "glass"},
        "brand": {"id": 1, "brand": "jam 1 producter"},
        "stock_disponible": {"id": 2, "stock_disponible": "false"},
        "category": {"id": 1, "category": "Preserves"},
        "ingredients": [
            {
                "id": 1,
                "ingredient": {"id": 1, "ingredient": "sugar"},
                "quantity": 2.5,
                "product": 1,
            },
            {
                "id": 2,
                "ingredient": {"id": 2, "ingredient": "lemon juice"},
                "quantity": 1.0,
                "product": 1,
            },
        ],
        "name": "cerises",
        "description": "confiture à la cerises",
        "image": "cerises.jpeg",
        "price": "2",
        "promotion": 1,
        "quantity": 150.0,
    }
}

product_stock_indisponible = {
    "products": [
        {
            "id": 1,
            "name": "cerises",
            "description": "confiture à la cerises",
            "image": "cerises.jpeg",
            "price": "2",
            "flavor": 1,
            "type_contenant": 1,
            "category": 1,
        }
    ],
    "pages_number": 1,
}

products = {
    "products": [
        {
            "id": 1,
            "name": "cerises",
            "description": "confiture à la cerises",
            "image": "cerises.jpeg",
            "price": "2",
            "flavor": 1,
            "type_contenant": 1,
            "category": 1,
        },
        {
            "id": 2,
            "name": "figue",
            "description": "confiture à la figue",
            "image": "figue.jpeg",
            "price": "3",
            "flavor": 2,
            "type_contenant": 2,
            "category": 2,
        },
        {
            "id": 3,
            "name": "banane",
            "description": "confiture à la banane",
            "image": "figue.jpeg",
            "price": "7",
            "flavor": 2,
            "type_contenant": 2,
            "category": 2,
        },
        {
            "id": 4,
            "name": "abricot",
            "description": "confiture à abricot",
            "image": "figue.jpeg",
            "price": "5",
            "flavor": 2,
            "type_contenant": 2,
            "category": 2,
        },
    ],
    "pages_number": 1,
}
