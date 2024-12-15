from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.warna = warna
    

    def info_burung(self):
        super().info_Animal(),
        print("Paruh  \t\t: ",self.paruh,
              "\nwarna\t\t: ",self.warna)

burung_beo = Burung("beo", "jagung", "udara", "bertelur", "melengkung", "warna-warni")
burung_beo.info_burung()
print("==============================================")

burung_merpati = Burung("merpati", "jagung kering", "udara", "bertelur" , "lurus", "putih")
burung_merpati.info_burung()
        
