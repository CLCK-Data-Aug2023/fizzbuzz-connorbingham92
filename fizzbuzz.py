for i in range(1,101):
    #check to see if each number is divisible by both 3 and 5
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    #check to see if number is divisible by 3
    elif(i%3==0):
        print("Fizz")
    #check to see if number is divisible by 5
    elif(i%5==0):
        print("Buzz")
    #when number is not divisible by either, print i
    else:
        print(i) # add your code here

