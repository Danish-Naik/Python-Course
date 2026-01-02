#Function 
def group(): #Declaration of the function 
    print("Group 1") #

group() #Callingf of the function 

#Arguments 

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")  #parameters

greet("Danish", "Naik") #Passing of the values

#Type of function 
#There are two types of hfunction 
#1. Perform a task
#2. Return a value

def get_greet(name):
    return f"Hello {name}"  #Return value

print(get_greet("Danish"))  #Calling the function and printing the return value