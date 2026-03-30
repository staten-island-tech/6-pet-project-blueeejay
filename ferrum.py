sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]
# def reciepts(EATEN):
#     truereciept = {}
#     total = 0
#     for item in EATEN: 
#         if item["name"] not in truereciept:
#             truereciept['roll'] = EATEN[item]["name"] 
#             total =+ EATEN["price"]
#         if ["name"] in truereciept:
#             total =+ EATEN["price"]
#     print(truereciept, total)
# reciepts(sushi_orders)


def reciepts(EATEN):
    truereciept = {}
    total = 0
    for item in EATEN: 
        if item["name"] in truereciept:
            'quantity' =+ 1 
        else:
            truereciept[item['name']] = {
            'price': item['price']
            "quantity": 1 }

    print(truereciept, total)
reciepts(sushi_orders)