input1=open("abc.txt","r")
content=input1.readlines()
output1=open("cba.txt","w")
for i in range(0,len(content)):
    if(i%2!=0):
        output1.write(content[i])
    else:
        pass
input1.close()
output1.close()
fp=open("cba.txt","r")
cont=fp.readlines()
print(cont)
fp.close()