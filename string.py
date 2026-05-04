s=input("enter a string")
result=""
i=0
while i<len(s):
    letter=s[i]
    num=int(s[i+1])
    result=result+letter*num
    i=i+2
print("output:",result)
