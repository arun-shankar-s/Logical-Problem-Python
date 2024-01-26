a=input("Enter a String:")
n=len(a)

for i in range(1,n+1,1):
    print(i,":")
    for j in range(0,n,i):
        if(j+i)<=n:
            print(a[j:j+i])
        else:
            print("No More",i,"pair Combination")
    print()
print("End of the Combination")
