#write a program to find the factorial of a nummber
n = int(input('enter a number: '))
f = 1
for i in range(1, n+1):
    f *= i
print(f) 
