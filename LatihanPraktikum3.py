class Kendaraan:
    # Class attribute (dimiliki oleh semua objek dari class ini)
    bahan_bakar = "Bensin"

    # Constructor untuk inisialisasi instance attributes
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"Kendaraan {self.merk} berwarna {warna_helper(self.warna)} keluaran tahun {self.tahun}"

# Helper sederhana untuk kerapihan teks
def warna_helper(warna):
    return warna

# Instansiasi object Kendaraan
kendaraan1 = Kendaraan("Toyota Avanza", "Hitam", 2022)
kendaraan2 = Kendaraan("Honda Beat", "Putih", 2023)

# 1. Demonstrasi Instance Attribute (unik untuk setiap objek)
print("--- Akses Instance Attribute ---")
print(f"Merk 1: {kendaraan1.merk}, Warna: {kendaraan1.warna}, Tahun: {kendaraan1.tahun}")
print(f"Merk 2: {kendaraan2.merk}, Warna: {kendaraan2.warna}, Tahun: {kendaraan2.tahun}")

# 2. Demonstrasi Class Attribute (diakses melalui Nama Class maupun Objek)
print("\n--- Akses Class Attribute ---")
print(f"Akses via Class (Kendaraan): {Kendaraan.bahan_bakar}")
print(f"Akses via Objek 1 (kendaraan1): {kendaraan1.bahan_bakar}")
print(f"Akses via Objek 2 (kendaraan2): {kendaraan2.bahan_bakar}")

# 3. Demonstrasi perubahan Class Attribute
print("\n--- Perubahan Class Attribute ---")
Kendaraan.bahan_bakar = "Pertalite"
print(f"Setelah diubah via Class, bahan bakar kendaraan1: {kendaraan1.bahan_bakar}")
print(f"Setelah diubah via Class, bahan bakar kendaraan2: {kendaraan2.bahan_bakar}")



