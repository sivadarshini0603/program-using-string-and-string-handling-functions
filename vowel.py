s=input("enter a string")
v=0
c=0
for ch in s:
    if ch in "aeiouAEIOU":
        v+=1
    elif ch.isalpha():
        c+=1
print("vowels:",v)
print("consonants",c)
