def rerata(b=[]):
    x=0
    n=0
    if b != []:
        for i in b:
            x+=i
            n+=1
        return x/n
z=rerata([1,2,3,4,5])
print(z)

g=[3,4,5,4,3,4,5,2,2,10,11,23]
r=rerata(g)
print(r)
