class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}."

# Instansiasi 2 object dosen
dosen1 = Dosen("Dr. Ahmad Fauzi", "0011223344")
dosen2 = Dosen("Siti Rahma, M.Kom.", "0055667788")

# Memanggil method
print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Struktur Data"))

