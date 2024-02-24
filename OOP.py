#class
class Mobil:
    pass

class Kendaraan:
    rode = 2

#attribute
class Mobil:
    warna = "merah"
    kecepatan = 0

Mobil1 = Mobil ()
print(Mobil.warna)

#constractor
class Mobil:
    def __init__(self, warna, kecepatan):
        self.warna = warna
        self.kecepatan = kecepatan

    warna = "merah"
    kecepatan = 0

    def tambah_kecepatan (self, kecepatan) :
        self.kecepatan = kecepatan

    def kurang_kecepatan(self, kecepatan) :
        self.kecepatan

mobil1 = Mobil ("Red", 999)
print(mobil1.warna)

mobil2 = Mobil ("blue", 500)
print(mobil2.warna)

#instance
