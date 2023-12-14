ls=[]
sum=0
n=(int(input("Enter the Size")))

for i in range(n):
    ls.append((int(input("Enter the Number"))))
    sum=sum+ls[i]

print(sum)