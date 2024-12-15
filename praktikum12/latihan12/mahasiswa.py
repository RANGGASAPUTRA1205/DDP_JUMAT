from parent import person

class mahasiswa (person):
    def __init__(self, nama, gender, umur, prodi, semester):
        super().__init__(nama, gender, umur)
        self.prodi = prodi
        self.semester = semester
    def cetak(self):
        super().cetak()
        print("prodi \t\t :",self.prodi,
              "\nsemester \t\t :",self.semester,
              "\n====================================")