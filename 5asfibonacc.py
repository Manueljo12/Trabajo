a,b = 0,1
n = 5

if n == 0:
    print(0)
elif n == 1:
    print(b)
else:
    for i in range(0,n):
        print(b)
        c = a + b
        a = b
        b = c