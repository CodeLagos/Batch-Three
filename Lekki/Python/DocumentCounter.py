str=input("input your document")
d=l=s=o=0
for c in str:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1
    elif c.isspace():
        s = s + 1
    else:
        o = o + 1
print("letters", l)
print("digits", d)
print("space", s)
print("other", o)
