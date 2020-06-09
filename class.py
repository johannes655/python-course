class Sawo:
    def __init__(self, nama, umur,berat):
        self.nama = nama
        self.umur = umur
        self.berat = berat

siswa = Sawo("Leo", 17, 60)
print (siswa.nama)
print (siswa.umur)
print (f"{siswa.berat} Kg")
