 
import random
lower =  "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,@#._-"
all = lower + upper + numbers + symbols
length = int(input("Enter the length of your password: \n"))
password = "".join(random.sample(all, length))
print(password)