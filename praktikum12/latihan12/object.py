from mahasiswa import *
from dosen import *

m1 = mahasiswa("afif", "pria", 20, "SI", "semester 3")
m2 = mahasiswa("jaenab", "wanita", 25, "TI", "semester 5")
d1 = dosen("ujang", "pria", 40, "st.r.kom", "LPPM")
d2 = dosen ("intan", "wanita", 30, "m.kom", "LTSI")

d1.setGaji(12000000)
d2.setGaji(10000000)

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()