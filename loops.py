# for loop
for number in range(1, 16, 2):
    print("Beautiful", number) # For repeating a particular code/ function

# For/Else Loop
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed") # For executing a else statement if the for loop is not early terminated.

# Nested For Loop
for x in range(5):
    for y in range(3):
        print(f"({x},{y})") #Having a for loop inside a for loop.

# Iterable
for x in "Python":
    print(x)
for y in [1, 2, 3, 4]:
    print(y) #The object that are iterable that is repeatable having different values each time is being executed.

# While Loop
number = 100
while number > 0:
    print(number)
    number //= 2  # augmented assignment operator #Excecuted until the condition is true/false.

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command) 

#Infinite Loop
while True:
    command = input(">")
    if command.lower() == "quit":
        break # Does not a fixed range but is not used usualy without the break statement.
    