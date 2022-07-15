print("Nama  : Ahmad Darmawan")
print("NIM   : 191011400381")

def turun(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)

def naik(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

def s_rendah(y, ysr, yr):
    return (y - ysr) / (yr - ysr)


def rendah(y, yr, ys):
    return (y - yr) / (ys - yr)

def standar(y, ys, yt):
    return (y - ys) / (yt - ys)


def tinggi(y, yt, yst):
    return (y - yt) / (yst - yt)


def s_tinggi(y, yt, yst):
    return (y - yt) / (yst - yt)


class penjualan_harian():
    minimum = 11
    maximum = 50

    def turun(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)


#sangat rendah =sr
#rendah = r
#standar = s
#tinggi = t
#sangat tinggi = s

class penjualan_bulanan():
    s_rendah = 11
    rendah = 15
    standar = 25
    tinggi = 30
    atas = 50

    def s_rendah(self, y):
        if y >= self.rendah or y<= self.s_rendah:
            return 0
        elif self.s_rendah < y < self.rendah:
            return up(y, self.s_rendah, self.standar)

        else:
            return 1
    
    def rendah(self, y):
        if y >= self.standar or y<= self.rendah:
            return 0
        elif self.s_rendah < y < self.rendah:
            return up(y, self.s_rendah, self.standar)
        elif self.standar < y < self.tinggi:
            return down(y, self.standar, self.tinggi)
        else:
            return 1
    
    def standar(self, y):
       if y >= self.tinggi or y<= self.standar:
             return down(y, self.standar, self.tinggi)
        else:
            return 1
        

    
    def tinggi(self, y):
    if y >= self.tinggi or y<= self.standar:
            return down(y, self.standar, self.tinggi)
        else:
            return 1
            
    


class nilai_akhir():
    minimum = 50
    maximum = 90
  penjualan_harian = 0
  penjualan_bulanan = 0

    def _menurun(self, a):
        return self.maximum - a*(self.maximum - self.minimum)

    def _meningkat(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def _inferensi(self, ph=penjualan_harian(), pb=penjualan_bulanan()):
        result = []
        # [R1] JIKA nilai harian turun, dan nilai kelompok sangat rendah, MAKA
        # nilai akhir menurun.
        a1 = min(ph.turun(self.penjualan_harian), pb.s_rendah(self.penjualan_bulanan))
        z1 = self._menurun(a1)
        result.append((a1, z1))
        # [R2] JIKA nilai harian TURUN, dan nilai kelompok rendah, MAKA
        # nilai akhir menurun.
        a2 = min(ph.turun(self.penjualan_harian), pb.rendah(self.penjualan_bulanan))
        z2 = self._menurun(a2)
        result.append((a2, z2))
        # [R3] JIKA nilai harian TURUN, dan nilai kelompok standar, MAKA
        # nilai akhir menurun.
        a3 = min(ph.turun(self.penjualan_harian), pb.standar(self.penjualan_bulanan))
        z3 = self._menurun(a3)
        result.append((a3, z3))
          # [R4] JIKA nilai harian TURUN, dan nilai kelompok tinggi, MAKA
        # nilai akhir meningkat.
        a4 = min(ph.turun(self.penjualan_harian), pb.tinggi(self.penjualan_bulanan))
        z4 = self._meningkat(a4)
        result.append((a4, z4))
        # [R5] JIKA nilai harian TURUN, dan nilai kelompok sangat tinggi, MAKA
        # nilai akhir meningkat.
        a5 = min(ph.turun(self.penjualan_harian), pb.s_tinggi(self.penjualan_bulanan))
        z5 = self._meningkat(a5)
        result.append((a5, z5))
        # [R6] JIKA nilai harian naik, dan nilai kelompok sangat_rendah, MAKA
        # nilai akhir menurun.
        a6 = min(ph.naik(self.penjualan_harian), pb.s_rendah(self.penjualan_bulanan))
        z6 = self._menurun(a6)
         result.append((a6, z6))
         # [R7] JIKA nilai harian naik, dan nilai kelompok rendah, MAKA
        # nilai akhir menurun.
        a7 = min(ph.naik(self.penjualan_harian), pb.rendah(self.penjualan_bulanan))
        z7 = self.menurun(a7)
         result.append((a7, z7))
         # [R8] JIKA nilai harian naik, dan nilai kelompok standar, MAKA
        # nilai akhir bertambah.
        a8 = min(nh.naik(self.penjualan_harian), pb.standar(self.penjualan_bulanan))
        z8 = self.meningkat(a8)
        result.append((a8, z8))
         # [R9] JIKA nilai harian naik, dan nilai kelompok tinggi, MAKA
        # nilai akhir bertambah.
        a9 = min(nh.naik(self.penjualan_harian), nk.tinggi(self.penjualan_bulanan))
        z9 = self._bertambah(a9)
        result.append((a9, z9))
         # [R10] JIKA nilai harian naik, dan nilai kelompok sangat_tinggi, MAKA
        # nilai akhir bertambah.
        a10 = min(nh.naik(self.penjualan_harian), nk.tinggi(self.penjualan_bulanan))
        z10 = self._bertambah(a9)
        result.append((a10, z10))
        return data_inferensi:
        return result():
    
    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4+a5*z5+α6∗z6+α7∗z7+α8∗z8+α9∗z9+a10*z10) / (α1+α2+α3+α4+a5+a6+a7+a8+a9+a10)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a 
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a