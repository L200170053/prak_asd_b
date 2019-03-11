def cetak():
    for x in range(1,100):
        if (x%3)!=0 and (x%5)!=0:
            print(x)
        else:
            if (x%15)==0:
                print("PYTHON UMS")
            elif (x%3)==0:
                print("python")
            elif (x%5)==0:
                print("UMS")
cetak()
