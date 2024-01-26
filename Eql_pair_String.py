a=input("Enter a string: ")

n=len(a)
for i in range(1,n+1,1):
    print(i,":")
    for j in range(n-(i-1)):
        print(a[j:j + i])
    print()
print("End of the combination")
