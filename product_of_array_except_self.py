//given integer array array,return an array answer such that answer[i]
is equal to the product of all the elements of array except array[i]













n = int(input("Enter The Size: "))
arr = []
answer=[]

for i in range(n):
    arr.append(int(input("Enter The Number: ")))

for i in arr:
    product = 1
    for j in arr:
        if i != j:
            product *= j

    answer.append(product)



print(answer)

	