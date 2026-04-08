def classify(number):
 if number < 1:
     raise ValueError("Classification is only possible for positive integers.")
 else:
     total = 0
     for i in range(1,number, 1):
         if(number % i  == 0):
             total = total + i

 if total < number:
     return "deficient"
 elif total > number:
     return "abundant"
 elif total == number:
     return "perfect"
     