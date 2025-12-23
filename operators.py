#Comparison Operators 
print("Basic Comparison operators are")
print("5>3:", 5>3)
print("16 != 11", 16 != 11)
print("86 == 86", 86 == 86)

print("each character have theirown value i.e ASCII value")
print(ord("D"))

print("bag" != "Baby")


#Conditional Statements - If/Else Statement
temperature = 12
if temperature > 30:
      print("It is hot")
      print("Drint it")
elif temperature > 20:
      print("It is warm")
else:
      print("It is cold")
print("Why you need hot water ?")

#Ternary Operator
#Writing a single line almost English like statement for ternary operator
age = 1
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

#Logical Operator 
#There are three logical operator - and, or, not 

#and Operator - Used for checking if the both the conditions are true or not.
high_income = True
low_income = False

if high_income and low_income: 
      print("You have a great job")
else:
      print("Change your job")

#or Operator - Used for checking even one statement is true or not.
time = 10
space = 5

if time>10 or space>6:
      print("You are immortal")
else:
      print("You are human being")

#not Operator - Used for having the opposite value of the condition.
student = True
if not student:
      print("You are not a student")
else:
      print("You are a student")

#Mix of all the statements / Short Circuit  Evaluation
#Making the logical operator in a more shorter version and the less time consuming.
if (high_income or low_income) and not student:
      print("Study First!!")
else:
      print("Grow Up boy")


#Chaining Comparison Operator 
#Making the comaprison operator shorter.

age = 20
if 18<= age < 75:
      print("Valid")
else:
      print("Invalid")

