import math
#### 
#explaining the formula 
print('The Fibonacci sequence is a series of integers (the Fibonacci numbers) that start with a zero, then a one, another one, then a series of rapidly increasing numbers. This formula enables us to identify a specific number (the nth term) in the sequence without having to carry out any long and hard math.')
####
#question
value_n = int(input('what is your value of n (the number you want to jump to)?  '))
if value_n < 2:
        print("value must be > or = 2, try again!")

####
#formula and result 
if value_n > 2:
 sqrt5 = math.sqrt(5)
 formula = int((( (1 + sqrt5) ** value_n - (1 - sqrt5) ** value_n ) / ( 2 ** value_n * sqrt5 )))
 result = formula 

 print('your value of n is', result)
 #"On my honor, I pledge that I have neither given nor received unauthorized information on this assignment. I did this work only for this assignment. If I have plagiarized, I will receive a zero for this project."