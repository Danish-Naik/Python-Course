# for loop
for number in range(1, 16, 2):
    print("Beautiful", number)

# For/Else Loop
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Nested For Loop
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

# Iterable
for x in "Python":
    print(x)
for y in [1, 2, 3, 4]:
    print(y)

# While Loop
number = 100
while number > 0:
    print(number)
    number //= 2  # augmented assignment operator

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

#Infinite Loop
while True:
    command = input(">")
    if command.lower() == "quit":
        break
    