def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    d=(b**2)-(4*a*c)
    if d<0:
        return "Determinannya negatif. Persamaan tidak mempunyai akar real"
    return  "Determinannya positif. Persamaan mempunyai akar real"
print(selesaikanABC(1,2,3))
