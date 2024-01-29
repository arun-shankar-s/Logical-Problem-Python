inp=input("Enter the String:")
inp=inp.lower()
count={}
v="a,e,i,o,u"
vowels=v.split(",")
for i in inp:
    if i in vowels:
        if i in count:
         count[i] += 1
        else:
         count[i] = 1
print (count)
