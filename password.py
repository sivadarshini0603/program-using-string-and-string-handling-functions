pwd=input("enter password")
d=False
l=False
u=False
s=False
sp=False
if len(pwd)<8 or len(pwd)>15:
    print("invalid password")
else:
    for ch in pwd:
        if ch=='':
            sp=True
        elif '0'<=ch<='9':
            d=True
        elif 'a'<=ch<='z':
            l=True
        elif 'A'<=ch<='Z':
            u=True
        elif ch in "@#$%!&":
            s=True
if not sp and d and l and u and s:
    print("valid")
else:
    print("not valid")

