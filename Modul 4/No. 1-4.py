class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSalu)\
            + '. tiap bulannya.'
        return s

c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTIF("Budi", 51, "Sragen", 230000)
c2 = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTIF("Chandra", 18, "Surakarta", 235000)
c4 = MhsTIF("Eka", 4, "Boyolali", 240000)
c5 = MhsTIF("Fandi", 31, "Salatiga", 250000)
c6 = MhsTIF("Deni", 13, "Klaten", 245000)
c7 = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTIF("Janto", 23, "Klaten", 245000)
c9 = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTIF("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#No. 1
def cariAsal():
    target = input("Masukkan kota: ")
    x = []
    for i in range (len(Daftar)):
        if target == Daftar[i].kota:
            x.append(i)
    print(x)

#No. 2
def cariUSTerkecil():
    terkecil = Daftar[0].uangSaku
    for i in range (len(Daftar)):
        if terkecil > Daftar[i].uangSaku:
            terkecil = Daftar[i].uangSaku
    return terkecil

#No. 3
def cariUSTerkecil2():
    terkecil = Daftar[0].uangSaku
    x = []
    a = cariUSTerkecil
    for i in range (len(Daftar)):
        if terkecil > Daftar[i].uangSaku:
            terkecil = Daftar[i].uangSaku
    
    for i in range (len(Daftar)):
        if Daftar[i].uangSaku == terkecil:
            x.append(Daftar[i].nama)
    return x

#No. 4
def carikurang25():
    a = 250000
    x = []
    for i in range(len(Daftar)):
        if Daftar[i].uangSaku < a:
            x.append(Daftar[i].nama)
    return x
            
