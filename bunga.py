class Bunga:
    def __init__ (self, nama, kelopak, harga) :
        self.nama = nama
        self.kelopak = kelopak
        self.harga = harga

    def kalimat(self):
        return f'Bunga {self.nama} memiliki {self.kelopak} kelopak dan harganya {self.harga}'

nama = input("Tuliskan Nama Bunga : ")
kelopak = input("Tentukan Jumlah Kelopak : ")
harga = input("Berapa Harga Satu Ikat Bunga : ")

harum = Bunga(nama, kelopak, harga)


print (harum.nama)
print (f"{harum.kelopak} helai")
print (f"{harum.harga} Rupiah")
print (harum.kalimat())
