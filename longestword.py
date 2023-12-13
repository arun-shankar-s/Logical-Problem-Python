l=[]

n=int(input("Enter the size of list "))

for i in range(n):
    l.append(input("Enter the elements"))

max=len(l[0])
temp=len[0]

for i in l:
    if l[i]>max:
        max=len(l[i])
        temp=l[i]

print("The longest word in the list is",temp,"which has",max,"characters")


