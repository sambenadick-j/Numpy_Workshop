#write a program to find the maximum of two numbers
n1 = int(input('enter no 1:'))
n2 = int(input('enter no 2:'))

res = n1 if n1 > n2 else n2
print(f'{res} is maximum of {n1} & {n2}')
res = max(n1, n2,461)
print(res)