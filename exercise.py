#Display the even numbers from 1 to 10 without using the step parameter. 
#Have the number of the even number at the end.
i = 0
for number in range(1,10):
    if(number % 2 == 0):
        print(number)

        i += 1
print(f"There are {i} even numbers")
