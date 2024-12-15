from parent import person
class dosen(person):

    def __init__(self, nama, gender, umur, gelar, jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan
    def setGaji(self,uang):
        self.gaji += uang
    def cetak(self):
        super().cetak()
        print("Gelar \t\t :",self.gelar,
              "\nJabatan \t\t :",self.jabatan,
              "\nGaji \t\t : RP.",self.gaji,
              "\n=================================")