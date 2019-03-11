def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",-6:"ratus ",-7:"juta ",8:"puluhjuta "}
    b=str(a)
    z=""
    i=-1
    while i>= -len(b):
        z=x[b[i]]+y[i]+z
        i-=1
    return z
print(katakan(3125750))
