#write a program to find the sum of digits of a given number'
n = int(input('enter a number: '))
n = str(n)
n = list(n)
print(sum(map(int,n)))