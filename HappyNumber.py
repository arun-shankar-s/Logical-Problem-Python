def function(a):
    sum = 0
    count=count+1
    while a != 0:
        rem = a % 10
        sum += rem * rem
        a = a // 10
    return sum

b = int(input("Enter a Number: "))
temp = function(b)

while temp != 1 and temp != 4:
    
    temp = function(temp)

if temp == 4:
    print("Not a Happy Number, Count:",count)
else:
    print("Happy Number, Count:", count)
