n=(int(input("Enter the Size")))
count=1
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(i*count, end=" ")
        count=count+1
    count=1    
    print()