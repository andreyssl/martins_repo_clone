# Dictionary
car = {"brand": "BMW", "model": "M5", "year": 2024, "price": 100000}
person = {"name": "Andrey", "age": 20, "car": "BMW"}

print(car)
print(person)


## access value by key
print(car["brand"])  # BMW
print(car["model"])  # M5
print(person["name"])  # Andrey
print(person.get("age"))  # 20


## modify value by key
car["price"] = 120000
print(car)  # price changed to 120000

person["age"] = 21
print(person)  # age changed to 21


## modify value by key

car["color"] = "Black"
print(car)  # new key color added

person["city"] = "Paris"
print(person)  # new key city added
