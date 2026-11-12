# Strings
string = "Cristiano Ronaldo SUIIIII"
print(string)
string = "Messi is a clown"
print(string.upper())

## indexing
print(string.index("a"))

## slice
print(string[2:5])

## length
print(f"{string} lenght is {len(string)}")

## concatenation (f-strings)
first_name= "Andrey"
last_name= "Zalivakin"
age=20
print(first_name + " " + last_name)
print(f"Full name: {first_name} {last_name}, age: {age}")


## uppercase / lowercase / title / strip
some_text="   Python Programming lecture till 19:30"
print(some_text.lower())
print(some_text.upper())
print(some_text.title())
print(some_text.strip())

## find()

print(some_text.find("lecture"))