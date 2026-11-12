
# loops
cars = ["BMW", "Bentley", "Mercedes", "Rolls Royce", "Porsche"]
numbers = [1,2,3,4,5,6,7,8,9,10]


## while
i = 0
while i < 5:
    print(i)  # 0,1,2,3,4
    i += 1

i = 0
while i < len(cars):
    print(cars[i])  # print each car
    i += 1

number = 5
while number > 0:
    print(number)  # 5,4,3,2,1
    number -= 1


## for

for car in cars:
    print(car)  # print each car

for number in numbers:
    print(number)  # print numbers from 1 to 10

for i in range(5):
    print(i)  # 0,1,2,3,4

for i in range(1, 6):
    print(i)  # 1,2,3,4,5

for i in range(0, 10, 2):
    print(i)  # 0,2,4,6,8


## break / continue

for car in cars:
    if car == "Mercedes":
        break  # stop loop when mercedes is found
    print(car)

for car in cars:
    if car == "Bentley":
        continue  # skip bentley
    print(car)


## enumerate()

for index, car in enumerate(cars):
    print(index, car)  # print index and car name


## nested loops

for car in cars:
    for number in range(1, 4):
        print(car, number)  # print each car 3 times
