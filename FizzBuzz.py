#Print numbers from 1-100
for i in range(1,101):
#if multiple of 3 and 5 print "FizzBuzz"    
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
#If multiple of 3 print "Fizz"
    elif i % 3 == 0:
        print("Fizz")
#If multiple of 5 pring "Buzz"
    elif i % 5 == 0:
        print("Buzz")
#Print all other integers
    else:
        print(i)