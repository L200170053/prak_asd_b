#Program by Kelompok Susi Triana Wati,Program Pencarian Serta Pengurutan dengan Bubble Sort.
from Tkinter import Tk,Frame,Menu
from Tkinter import*
import tkMessageBox as psn
import ttk
import tkFileDialog as bk
from tkMessageBox import *
import Tkinter as tk
from winsound import *
import platform
os = platform.system()


class MouseWheel(object): # Kelas untuk mengatur scroolbar
    def __init__(self, root, factor = 2):
        global os
        
        self.activeArea = None
        
        if type(factor) == int:
            self.factor = factor
        else:
            raise Exception("Factor must be an integer.")

        if os == "Linux" :
            root.bind_all('<4>', self.onMouseWheel,  add='+')
            root.bind_all('<5>', self.onMouseWheel,  add='+')
        else:
            # Windows and MacOS
            root.bind_all("<MouseWheel>", self.onMouseWheel,  add='+')

    def onMouseWheel(self,event):
        if self.activeArea:
            self.activeArea.onMouseWheel(event)

    def mouseWheel_bind(self, widget):
        self.activeArea = widget

    def mouseWheel_unbind(self):
        self.activeArea = None

    @staticmethod
    def build_function_onMouseWheel(widget, orient, factor = 1):
        view_command = getattr(widget, orient+'view')
        if os == 'Linux':
            def onMouseWheel(event):
                if event.num == 4:
                    view_command("scroll",(-1)*factor,"units" )
                elif event.num == 5:
                    view_command("scroll",factor,"units" ) 
                
        elif os == 'Windows':
            def onMouseWheel(event):        
                view_command("scroll",(-1)*int((event.delta/120)*factor),"units" ) 
        
        elif os == 'Darwin':
            def onMouseWheel(event):        
                view_command("scroll",event.delta,"units" )             
        
        return onMouseWheel
        

    def add_scrolling(self, scrollingArea, xscrollbar=None, yscrollbar=None):
        scrollingArea.bind('<Enter>',lambda event: self.mouseWheel_bind(scrollingArea))
        scrollingArea.bind('<Leave>', lambda event: self.mouseWheel_unbind())

        if xscrollbar and not hasattr(xscrollbar, 'onMouseWheel'):
                setattr(xscrollbar, 'onMouseWheel', self.build_function_onMouseWheel(scrollingArea,'x', self.factor) )

        if yscrollbar and not hasattr(yscrollbar, 'onMouseWheel'):
                setattr(yscrollbar, 'onMouseWheel', self.build_function_onMouseWheel(scrollingArea,'y', self.factor) )

        active_scrollbar_on_mouse_wheel = yscrollbar or xscrollbar
        if active_scrollbar_on_mouse_wheel:
            setattr(scrollingArea, 'onMouseWheel', active_scrollbar_on_mouse_wheel.onMouseWheel)

        for scrollbar in (xscrollbar, yscrollbar):
            if scrollbar:
                scrollbar.bind('<Enter>', lambda event, scrollbar=scrollbar: self.mouseWheel_bind(scrollbar) )
                scrollbar.bind('<Leave>', lambda event: self.mouseWheel_unbind())


class simpul():
    '''Membuat kelas simpul''' 
    def __init__(self, data=None):
        self.data = data
        self.link = None


class Tugas_GUI(Frame):
    '''Membuat kelas GUI'''
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.list = None

        # membuat canvas pada frame utama
        self.canvas = Canvas(parent, background="grey") 
        self.frame = Frame(self.canvas, background="purple") 

        # mengedit style untuk scrollbar
        s = ttk.Style()
        s.theme_use('classic')
        s.configure("coba.Vertical.TScrollbar", foreground = 'pink',background='teal')

        # membuat scrollbar pada canvas
        self.vsb = ttk.Scrollbar(parent, style="coba.Vertical.TScrollbar", orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", 
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.OnFrameConfigure)

        # agar scrool bar dapat di scroll
        MouseWheel(root).add_scrolling(self.canvas, yscrollbar=self.vsb) 

    def OnFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=400)
       

    def initUI(self):
        self.parent.title("Tabel Data Item Di Toko Alat Tulis Kampus")
        menubar = Menu(self.parent)      
        self.parent.config(menu = menubar, bg = 'purple')

        # Membuat dan mengatur Button dan frame
        self.btnKeluar = Button(self.parent,cursor = 'pirate',text="\n\n\n\nK\n\nE\n\nL\n\nU\n\nA\n\nR\n\n\n\n",
                                relief=RIDGE, bd=5, bg='burlywood',
                                fg='red',command=self.onExit)
        self.btnKeluar.pack(side=RIGHT, fill=X)

        self.btnimpor = Button(self.parent,text="\n\n\n\nI\n\nM\n\nP\n\nO\n\nR\n\nT\n\n\n\n",
                                relief=RIDGE, bd=5, bg='burlywood',
                                fg='red',command=self.impor)
        self.btnimpor.pack(side=LEFT, fill=X)

        fr_atas = Frame(self.parent)
        fr_atas.pack(fill = BOTH)

        
        self.btnnomor = Button(fr_atas,text="NO",
                                 bd=1, bg='brown', width=14,
                                fg='green',command=self.nomor)
        self.btnnomor.pack(side=LEFT, fill=BOTH)
        self.btnnomor.configure(state=DISABLED)

        self.btntanggal = Button(fr_atas,text="TANGGAL CEK",
                                 bd=1, bg='brown',width=14,
                                fg='green',command=self.nomor)
        self.btntanggal.pack(side=LEFT, fill=BOTH)
        self.btntanggal.configure(state=DISABLED)

        self.btnnama = Button(fr_atas,text="NAMA BARANG",
                                 bd=1, bg='brown',width=14,
                                fg='green',command=self.nama)
        self.btnnama.pack(side=LEFT, fill=BOTH)
        self.btnnama.configure(state=DISABLED)

        self.btnjumlah = Button(fr_atas,text="JUMLAH BARANG",
                                 bd=1, bg='brown',width=14,
                                fg='green',command=self.jumlah)
        self.btnjumlah.pack(side=LEFT, fill=BOTH)
        self.btnjumlah.configure(state=DISABLED)

        self.btnharga = Button(fr_atas,text="HARGA BARANG",
                                 bd=1, bg='brown',width=14,
                                fg='green',command=self.harga)
        self.btnharga.pack(side=LEFT, fill=BOTH)
        self.btnharga.configure(state=DISABLED)

        self.btnmodal = Button(fr_atas,text="MODAL",
                                 bd=1, bg='brown',width=14,
                                fg='green',command=self.modal)
        self.btnmodal.pack(side=LEFT, fill=BOTH)
        self.btnmodal.configure(state=DISABLED)

        self.btnsales = Button(fr_atas,text="SALES",
                                 bd=1, bg='brown',width=14,
                                fg='green',command=self.sales)
        self.btnsales.pack(side=LEFT, fill=BOTH)
        self.btnsales.configure(state=DISABLED)

        self.btncari = Button(self.parent,cursor = 'target',text="CARI",
                                 bd=5, bg='burlywood',
                                fg='red',command=self.carisemua)
        self.btncari.pack(side=BOTTOM, fill=X)
        self.btncari.configure(state=DISABLED)
        

        self.lblStatus = Button(self.parent,
                        text='TAMPILKAN',
                                  bd=5,fg='red',bg='pink',command=self.tampilkan)
        self.lblStatus.pack(side=BOTTOM, fill=X)
        self.lblStatus.configure(state=DISABLED)

    def kejadian(self): # Fungsi Mengubah Button menjadi aktif
        self.btncari.configure(state=NORMAL)
        self.btnnomor.configure(state=NORMAL)
        self.btntanggal.configure(state=NORMAL)
        self.btnnama.configure(state=NORMAL)
        self.btnjumlah.configure(state=NORMAL)
        self.btnharga.configure(state=NORMAL)
        self.btnmodal.configure(state=NORMAL)
        self.btnsales.configure(state=NORMAL)

    def carisemua(self):    # Fungsi untuk pencarian data
##        p=self.list
        def show_entry_fields():   
            coba = []  
            cek = False
            p=self.list
            while p.link is not None:
                p=p.link
                if p.data.no == target.get()or \
                   p.data.tanggal[:2] == target.get() or p.data.tanggal[3:5] == target.get() or p.data.tanggal[6:] == target.get() or \
                   p.data.nama == target.get() or \
                   p.data.jumlah == target.get() or \
                   p.data.harga == target.get() or \
                   p.data.modal == target.get() or \
                   p.data.sales == target.get():
                    data = (p.data.no,p.data.tanggal,p.data.nama,p.data.jumlah,p.data.harga,p.data.modal,p.data.sales.rstrip('\n'))
                    coba.append(data)
                    
                    cek=True

            p=self.list
            while p.link is not None:
                p=p.link
                if p.data.no != target.get()and \
                   p.data.tanggal[:2] != target.get() and p.data.tanggal[3:5] != target.get() and p.data.tanggal[6:] != target.get() and \
                   p.data.nama != target.get() and \
                   p.data.jumlah != target.get() and \
                   p.data.harga != target.get() and \
                   p.data.modal != target.get() and \
                   p.data.sales != target.get():
                        coba.append(('','','','','','',''))

            
            if cek == False:
               psn.showwarning("Peringatan !", "Data Tidak Sesuai")

            data_tampil = coba
            for bariske in range(len(coba)):
                baris = data_tampil[bariske]
                for kolomke in range(len(coba[0])):
                    nilai = baris[kolomke]
                    widget = self._widgets[bariske][kolomke]
                    widget.configure(text=nilai)

        
        cari = Tk()
        cari.title('PENCARIAN DATA')
        cari.config(bg='grey')
        Label(cari, text="Masukan Data Yang Ingin Di Cari",fg='dark blue',bg='light blue').grid(row=0)
        target = Entry(cari)
        target.grid(row=0, column=1)        
        Button(cari, text='batal', command=cari.destroy,bg='#ff0000',fg='white').grid(row=3, column=1, sticky=W, padx=20,ipadx=30,pady=4)
        Button(cari, text=' cari ', command=show_entry_fields,bg='red',fg='white').grid(ipadx=30,row=3, column=0, sticky=W, padx=15)

        mainloop( )

    
    def diam(self):
        pass

    def tampilsortir(self):             # Fungsi untuk menampilkan hasil sortiran
        data_tampil = self.data_mhs
        for row in range(self.rows):
            baris = data_tampil[row]
            for column in range(self.columns):
                nilai = baris[column]
                widget = self._widgets[row][column]
                widget.configure(text=nilai)


############################## pengurutan data menggunakan Bubble Sort ####################################
    def bubbleSort(self,Data,indeks):
        '''fungsi untuk mengurutkan data dengan Bubble Sort
        input berupa list bernama Data'''
        n = len(Data)  # n adalah jumlah data

        #mengurutkan berdasarkan atribut nomor
        if indeks == 'nomor':
          for k in range(1,n):                                      # ulangi sebanyak n-1 kali
              for i in range(n-1):                                  # lakukan dari posisi paling kiri hingga ke kanan
                  if int(Data[i].data.no) > int(Data[i+1].data.no): # bandingkan dua data yang berdekatan
                      Data[i], Data[i+1] = Data[i+1], Data[i]       # menukar posisi data

        #mengurutkan berdasarkan atribut nama
        elif indeks == 'nama':
          for k in range(1,n):  
              for i in range(n-1):   
                  if (Data[i].data.nama) > (Data[i+1].data.nama):  
                      Data[i], Data[i+1] = Data[i+1], Data[i]

        #mengurutkan berdasarkan atribut jumlah
        elif indeks == 'jumlah':
          for k in range(1,n):  
              for i in range(n-1):   
                  if int(Data[i].data.jumlah) > int(Data[i+1].data.jumlah):  
                      Data[i], Data[i+1] = Data[i+1], Data[i]

        #mengurutkan berdasarkan atribut harga
        elif indeks == 'harga':
          for k in range(1,n):  
              for i in range(n-1):   
                  if int(Data[i].data.harga) > int(Data[i+1].data.harga):  
                      Data[i], Data[i+1] = Data[i+1], Data[i]

        #mengurutkan berdasarkan atribut modal
        elif indeks == 'modal':
          for k in range(1,n): 
              for i in range(n-1):  
                  if int(Data[i].data.modal) > int(Data[i+1].data.modal):  
                      Data[i], Data[i+1] = Data[i+1], Data[i]

        #mengurutkan berdasarkan atribut sales
        elif indeks == 'sales':
          for k in range(1,n): 
              for i in range(n-1):  
                  if (Data[i].data.sales) > (Data[i+1].data.sales):  
                      Data[i], Data[i+1] = Data[i+1], Data[i]
        
    def bubble(self,LL,indeks):
        '''mengurutkan linked list dengan Bubble Sort
        Tricky: dengan mengkonversi linked menjadi array, bubble sort lalu
        dikembalikan menjadi array'''
        # konversi dari Linked List ke python list
        li = []
        p = LL.link
        while p != None:
            li.append(p)
            p = p.link
        # memanggil fungsi bubble sort
        self.bubbleSort(li,indeks)
        # konversi dari python list ke Linked List
        p = LL
        for simpul in li:
            p.link = simpul
            simpul.link = None
            p = p.link
        p=LL.link
        self.data_mhs = []
        while p is not None:
            data=(p.data.no,p.data.tanggal,p.data.nama,p.data.jumlah,p.data.harga,p.data.modal,p.data.sales.rstrip('\n'))
            self.data_mhs.append(data)
            p=p.link

    def nomor(self):                    # Fungsi untuk mengurutkan nomor
            data = self.list_tampil
            self.bubble(data,'nomor')
            self.tampilsortir()

    def nama(self):                     # Fungsi untuk mengurutkan nama barang
            data=self.list_tampil
            self.bubble(data,'nama')
            self.tampilsortir()

    def jumlah(self):                   # Fungsi untuk mengurutkan jumlah barang
            data=self.list_tampil
            self.bubble(data,'jumlah')
            self.tampilsortir()

    def harga(self):                    # Fungsi untuk mengurutkan harga barang
            data=self.list_tampil
            self.bubble(data,'harga')
            self.tampilsortir()

    def modal(self):                    # Fungsi untuk mengurutkan modal
            data=self.list_tampil
            self.bubble(data,'modal')
            self.tampilsortir()

    def sales(self):                    # Fungsi untuk mengurutkan sales
            data=self.list_tampil
            self.bubble(data,'sales')
            self.tampilsortir()

    def impor(self):                    # Funsi untuk mengimport file csv
        try :
            File = bk.askopenfilename()
            x=open(File) # membuka file csv
            x.readline() # membaca file csv dengan mengabaikan baris pertama
            baca=x.readlines() #membaca semua data file csv dan menjadikannya sebuah list didalam variabel 'baca'  

            self.list = simpul() #self.list adalah kepala dari linked list yang akan dibuat ==> berisi None
            p=self.list       

            for k in range (len(baca)):                                 #
                z=baca[k].split(';')                                    #
                L=data_transaksi(z[0],z[1],z[2],z[3],z[4],z[5],z[6])    # membuat isi linked list
                p.link=simpul(L)                                        #
                p=p.link                                                #

            psn.showinfo("Pemberitahuan","import berhasil")
            x.close()
            self.list_tampil = self.list # membuat duplikat self.list
            self.lblStatus.configure(state=NORMAL) # mengaktifkan button tampilkan
        except IOError :
            psn.showwarning("Pemberitahuan","Import dibatalkan")
        except IndexError :
            psn.showwarning("Peringatan !","file anda tidak sesuai")


    def tampilkan(self): # Fungsi untuk menampilkan data
        try :
            p=self.list
            self.data_mhs = []
            while p.link is not None:
                
                data=(p.link.data.no,p.link.data.tanggal,p.link.data.nama,p.link.data.jumlah,p.link.data.harga,p.link.data.modal,p.link.data.sales.rstrip('\n'))
                self.data_mhs.append(data)
                p=p.link
                                
            # bagian yang ditambahkan untuk menampilkan data
            self.rows = len(self.data_mhs)  # jumlah baris
            self.columns = len(self.data_mhs[0])  # jumlah kolom
            self._widgets = list()
            for row in range(self.rows):
                self.current_row = list()
                for column in range(self.columns):
                    tampil = ''
                    label = Label(self.frame, text="%s" % tampil,  width=14, bg = 'black',fg = 'aqua')
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    self.current_row.append(label)
                self._widgets.append(self.current_row)
            for column in range(self.columns):
                self.grid_columnconfigure(column, weight=1)
            self.pack(side="top", fill="x")
            # akhir bagian yang ditambahkan untuk menampilkan data

            data_tampil = self.data_mhs
            for row in range(self.rows):
                baris = data_tampil[row]
                for column in range(self.columns):
                    nilai = baris[column]
                    widget = self._widgets[row][column]
                    widget.configure(text=nilai)
            self.kejadian()
            psn.showinfo("pemberitahuan","Berhasil Ditampilkan")
##            self.lblStatus.configure(state=DISABLED) # ini bisa di gunakan untuk maximize dan minimize
        except :
            psn.showwarning("Peringatan !", "Tidak ada file yang terbaca")
            

    def onExit(self):       # Fungsi untuk keluar dari program
        if askyesno('Peringatan!', 'Anda ingin keluar?'):
            play1 = PlaySound('ahem_x.wav', SND_FILENAME)
            self.parent.destroy()
        else:
            showinfo('Pemberitahuan', 'Keluar dibatalkan')




class data_transaksi():
    '''Membuat kelas data transaksi'''
    def __init__(self,no=None,tanggal=None,nama=None,jumlah=None,harga=None,modal=None,sales=None):
        self.no = no
        self.tanggal = tanggal
        self.nama    = nama
        self.jumlah  = jumlah
        self.harga   = harga
        self.modal   = modal
        self.sales   = sales

if __name__ =='__main__': # Untuk menjalankan Tkinter atau GUI 
    root = Tk() 
    root.geometry("813x294+400+400")
    root.resizable(False,False)
    app = Tugas_GUI(root)
    root.mainloop()





