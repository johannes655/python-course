class Persegi:
    def __init__ (self, panjang, lebar) :
        self.panjang = panjang
        self.lebar = lebar
        self.luas = panjang * lebar

    def itung (self):
        print (f'Luas Persegi Panjang anda sebesar {self.luas}')

panjang = int(input("Tentukan Panjang Dari Persegi Panjang Anda : "))
lebar = int(input("Tentukan lebar Dari Persegi Panjang Anda : "))

xoxo = Persegi (panjang, lebar)

xoxo.itung()
