# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".

# Tip: % (modulo) tells you what's left over when you divide one number by another
# ex. number % 3 == 0

for x in range(0,100):
    if (x%3==0 and x%5==0):
        print("FizzBuzz")
    elif(x%3==0):
        print("Fizz")
    elif(x%5==0):
        print("Buzz")
    else:
        print(x)