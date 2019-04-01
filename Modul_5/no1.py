Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class MhsTIF(object):
    def __init__(self, nama, NIM, alamat,us):
        self.nama = nama
        self.NIM = NIM
        self.alamat = alamat
        self.us = us

    def __str__(self):
        s = self.nama + "NIM" + str(self.NIM)\
            + ". Tinggal di " + self.alamat\
            + ". Uang Saku Rp. " + str(self.us)\
            + " Tiap Bulannya."
        
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
#Nomor1    
Daftar = [MhsTIF('Salsa', "L200170113", 'Madiun', 150000),
          MhsTIF('Lutfi', "L200170048", 'Karanganyar', 125000),
          MhsTIF('Fadel', "L200170078", 'Madiun', 20500),
          MhsTIF('Alvicky', "L200170065", 'Sragen', 350000),
          MhsTIF('Bayu', "L200170052", 'Sragen', 500000),
          MhsTIF('Kori', "L200170053", 'Surakarta', 430000),
          MhsTIF('Susi', "L200170047", 'Bojonegoro', 450000),
          MhsTIF('Rima', "L200170044", 'Klaten', 430000),
          MhsTIF('Sidiq', "L200170058", 'Klaten', 235000),
          MhsTIF('Yoga', "L200170034", 'Palur', 350000)]

def cekNIM(object):
    for i in object:
        print (i.NIM)
         
          
def urutNIM(object):
    n = len(object)
    for i in range(n-1):
        for j in range(n-i-1):
            if object[j].NIM > object[j+1].NIM:
                swap(object,j,j+1)
