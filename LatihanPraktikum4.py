class ManajerInventori:
    def __init__(self):
        # Dictionary untuk menyimpan data inventori {nama_barang: jumlah}
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        if jumlah > 0:
            if nama_barang in self.inventori:
                self.inventori[nama_barang] += jumlah
            else:
                self.inventori[nama_barang] = jumlah
            return f"Berhasil menambahkan {jumlah} {nama_barang}. Stok sekarang: {self.inventori[nama_barang]}"
        return "Jumlah penambahan harus lebih dari 0"

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori:
            if 0 < jumlah <= self.inventori[nama_barang]:
                self.inventori[nama_barang] -= jumlah
                # Jika stok habis, barang bisa dihapus dari dictionary
                if self.inventori[nama_barang] == 0:
                    del self.inventori[nama_barang]
                return f"Berhasil mengurangi/menghapus {jumlah} {nama_barang}."
            return f"Jumlah pengurangan melebihi stok yang ada! Stok saat ini: {self.inventori.get(nama_barang, 0)}"
        return f"Barang '{nama_barang}' tidak ditemukan di inventori."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori saat ini kosong."
        
        hasil = "--- Daftar Inventori ---"
        for barang, jumlah in self.inventori.items():
            hasil += f"\n- {barang}: {jumlah} unit"
        return hasil

# --- Pengujian / Demonstrasi Method ---
gudang = ManajerInventori()

# 1. Menambahkan barang
print(gudang.tambah_barang("Laptop Asus", 10))
print(gudang.tambah_barang("Mouse Logitech", 25))
print(gudang.tambah_barang("Laptop Asus", 5)) # Menambah stok barang yang sudah ada

print("\n" + "="*30 + "\n")

# 2. Melihat inventori
print(gudang.lihat_inventori())

print("\n" + "="*30 + "\n")

# 3. Mengurangi / menghapus sebagian stok barang
print(gudang.hapus_barang("Mouse Logitech", 5))

# 4. Melihat inventori setelah perubahan
print(gudang.lihat_inventori())


