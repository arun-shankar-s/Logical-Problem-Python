while(1):
    n=input("Enter the Number")
    b=len(n)
    c=int(n)
    a=c
    sum=0
    while(a!=0):
    	rem=a%10
    	sum=sum+(rem**b)
    	b=b-1
    	a=a//10
    if c==sum:
    	print("Dissarrium Number")
    else:
    	print("Not Dissarium")
