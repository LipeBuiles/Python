produts = {
    "name": "book",
    "price": 15000,
    "cuantity": 2
}

person = {
    "firt_name": "Juan Felipe",
    "last_name": "Builes"
}

print(person)
print(type(person))

#Methods with dir
print(produts.keys())
print(produts.items())

produts.clear()
print(produts)
#del produts
print(produts)

products = [
    {"name": "book", "price": 25000},
    {"name": "pc", "price": 1750000},
    {"name": "table", "price": 800000}
]
print(products)