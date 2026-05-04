s1=input().strip()
s2=input().strip()
if len(s1)==len(s2) and s2 in(s1+s1):
    print("its rotation")
else:
    print("no rotation")
