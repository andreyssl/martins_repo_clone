# lists
cars=["BMW", "Bentley", "Mercedes", "Rolls Royce", "Porsche"]
numbers = [1,2,3,4,5,6,7,8,9,10]
list_with_everything= ["Andrey", 20, True, "BMW", [1,2,4]]
print(cars, numbers, list_with_everything)
## indexing

print(cars[2]) #mercedes
print(list_with_everything[4]) # [1,2,4]
print(numbers[0]) #1

## slice
print(cars[1:4])      # ["Bentley", "Mercedes", "Rolls Royce"]
print(numbers[0:5])   # [1,2,3,4,5]
print(numbers[:3])    # [1,2,3]
print(cars[::-1])     # reversed cars list

## length
print(len(cars))                 # 5
print(len(numbers))              # 10
print(len(list_with_everything)) # 5
print(len(list_with_everything[4])) # 3

## append / insert / remove / pop
cars.append("Audi")
print(cars)  # audi added at the end

cars.insert(1, "Ferrari")
print(cars)  # ferrari added at index 1

cars.remove("Bentley")
print(cars)  # Bentley removed

cars.pop(2)
print(cars)  # mercedes removed

cars.pop()
print(cars)  # audi removed(last element)


## sort()
numbers.sort()
print(numbers)  # [1,2,3,4,5,6,7,8,9,10]

cars.sort()
print(cars)  # ["BMW", "Ferrari", "Porsche", "Rolls Royce"]

## tuples / sets
# tuple - ordered, cannot be changed
car_tuple = ("BMW", "Bentley", "Mercedes", "Porsche")

print(car_tuple)
print(car_tuple[0])    # BMW
print(car_tuple[-1])   # Porsche
print(len(car_tuple))  # 4

# car_tuple[0] = "Audi"  # Error! Tuples cannot be changed


# set - unordered, no duplicates
car_set = {"BMW", "Bentley", "Mercedes", "BMW", "Porsche"}

print(car_set)  # bmw appears only once
print(len(car_set))  # 4


car_set.add("Ferrari")  #add ferrari to set
print(car_set) 


car_set.remove("Bentley") #remove bentley element from set
print(car_set)






german_cars = {"BMW", "Mercedes", "Porsche"}
luxury_cars = {"Bentley", "Rolls Royce", "BMW"}

print(german_cars | luxury_cars)  # union- all unique cars
print(german_cars & luxury_cars)  # intersection- {"BMW"}
print(german_cars - luxury_cars)  # difference- {"Mercedes", "Porsche"}
