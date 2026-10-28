# variable
flower = "Yuzana"
print(f"Flower: {flower}")

# input
salary = float(input("Enter your salary: "))
print(f"My salary is ${salary}")

# loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in numbers:
    if n >= 5:
        print("Nothing is free.")
# fun
def callMe(name):
    print(f"I'm {name}!")
callMe("May")

# list
two_digit = [50, 21, 88]
two_digit[2] = 99
print("The second number is ", two_digit[2])

# tuple
fruits = ("apple", "orange", "watermelon")
print("Length of fruits: ", len(fruits))
for f in fruits:
    print(f)

# dictionary
vehicle = [
    {"name": "Kubota", "color": "Red", "wheel": 4},
    {"name": "Motorcycle", "color": "Black", "wheel": 2},
    {"name": "Bus", "color": "White", "wheel": 6}
]
for v in vehicle:
    if v["wheel"] <= 2:
        print(f"This is {v['name']}")