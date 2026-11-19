class Mahasiswa:
    # Class attribute (berlaku untuk semua objek)
    universitas = "STITEK Bontang"

    # Method konstruktor (__init__)
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        # Instance attributes
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method untuk menampilkan identitas mahasiswa
    def perkenalan_diri(self):
        print(f"Halo, nama saya {self.nama} (NIM: {self.nim}).")
        print(f"Saya dari jurusan {self.jurusan} di {Mahasiswa.universitas}.")
        print(f"IPK saat ini: {self.ipk:.2f}")

    # Method untuk memperbarui nilai IPK
    def update_ipk(self, ipk_baru):
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            print(f"[INFO] IPK {self.nama} berhasil diperbarui menjadi {self.ipk:.2f}.")
        else:
            print("[ERROR] Nilai IPK harus berada di antara 0.0 sampai 4.0.")

    # Method untuk menentukan predikat kelulusan berdasarkan IPK
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus / Perlu Perbaikan"


# ==========================================
# INSTANSIASI & DEMONSTRASI METHOD
# ==========================================

# Membuat 3 objek mahasiswa baru dengan data berbeda
mhs1 = Mahasiswa("Reza Pahlevi", "20240201", "Teknik Informatika", 3.82)
mhs2 = Mahasiswa("Nadia Putri Utami", "20240202", "Sistem Informasi", 2.75)
mhs3 = Mahasiswa("Dimas Saputra", "20240203", "Teknik Elektro")  # IPK default 0.0

print("=== DEMONSTRASI OBJEK 1 ===")
mhs1.perkenalan_diri()
print(f"Predikat Kelulusan: {mhs1.predikat_kelulusan()}\n")

print("=== DEMONSTRASI OBJEK 2 ===")
mhs2.perkenalan_diri()
print(f"Predikat Awal: {mhs2.predikat_kelulusan()}")
# Mengubah IPK mhs2 menggunakan method update_ipk
mhs2.update_ipk(3.40)
print(f"Predikat Setelah Update: {mhs2.predikat_kelulusan()}\n")

print("=== DEMONSTRASI OBJEK 3 ===")
mhs3.perkenalan_diri()
print(f"Predikat Awal: {mhs3.predikat_kelulusan()}")
# Mengisi IPK mhs3 yang awalnya default 0.0
mhs3.update_ipk(2.35)
print(f"Predikat Setelah Update: {mhs3.predikat_kelulusan()}")


