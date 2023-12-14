lst=[]
def func(n):
    for i in range(1,n//2,1):
        if i*i==n:
            lst.append(n)
            break
        

for i in range(1000,9999,1):
    if i%2==0:
        func(i)
print(lst)

