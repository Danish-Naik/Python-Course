# Variables : Allocates the memory space in the RAM for the given variable declaration.
students_count = 1000
rating = 4.99  # Floating Value
is_published = True  # Boolean Value is the value should be startig with the Capital letter
course_name = "Python Programmings"  # this is a string value

print(students_count)
print(course_name)

# Playing with strings
course = "Python Programming"
print(len(course))
print(course[0])  # First Character
print(course[-1])  # Automatically shifted to last character of the string
print(course[0:3])  # Selecting the characters from the index 0 to 2
# Selecting the characters from the index 0 to by default end of the string
print(course[0:])
# Selecting the characters from the by default start of the string to index 4
print(course[:3])
print(course[:])  # Copying the original string
# print(course[]) shows an error

# Escape Sequences
esp1 = "Hi \ Good Morning"
esp2 = "Hi \" Good Morning"
esp3 = "Hi \' Good Morning"
esp4 = "Hi \\ Good Morning"
esp5 = "Hi \n Good Morning"

print(esp1, esp2, esp3, esp4, esp5, sep="\n")

#Formatted String 
first = "Danish"
last = "Naik"
full = f"{first} {last}"
print(full)
message1 = "Good"
message2 = "Morning"
full = f"{message1} {message2}"
print(full)

#String Methods 

course = "  Python Programming"
print(course)
print(course.upper()) #Converts the string to uppercase
print(course.lower()) #Converts the string to lowercase
print(course.title()) #Converts the initial characters of the string to uppercase
print(course.strip()) #Removes the white spaces from the string from both right and left
print(course.rstrip()) #Removes the white spaces from the string from the right side of the string
print(course.lstrip()) #Removes the white spaces from the string from the left side of the string
print(course.find("pyt")) #If not found the value is returned as -1
print(course.find("Pyt")) #Finds the index of the given string
print(course.replace("o" , "k"))
print(("py" in course)) #finds if the word is present in the string or not and have the result as the boolean value
print("hello" not in course) #finds if the word is not present in the string or not.

#Numbers and Working with Numbers
print("We have the basic operators for the python such as +,-,*,/,%.") 
print("There are few  such as")
print(10 // 3) # Having only the integer value of the division
print(10 ** 3) # Having the power value of the given number such as 10 raise to 3

#Augmented Assignment Operators 
x = 5
x = x + 2
x =+ 2
print (x)

print("There are various basic function in the python such as")
print(round(8.8)) # Rounds of the number that is only the integer value of the floating number 
print(abs(-6)) # Gives of the positive value of the negative number

#If need of the more maths functions we can import the math module i.e import math
import math

#Type Conversion 
#Used for coverting the string to the different values such as integer, float, boolean
x = input("x:")
y = int(x) + 1
#print(f"x: {x}, y: {y}") #TypeError: can only concatenate str (not "int") to str
print(type(x))
print(f"x: {x}, y: {y}")
# Boolean Conversion will print the false value if the string is empty, null or having the value as 0.

#Escape Characters
print("Hello", sep ="..", end="\n")
print("World")