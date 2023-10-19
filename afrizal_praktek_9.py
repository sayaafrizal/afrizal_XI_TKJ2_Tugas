# Meminta input durasi peminjaman buku dalam hari
durasi_peminjaman = int(input("Masukkan durasi peminjaman buku dalam hari: "))

# Menentukan jenis pinjaman berdasarkan durasi
if durasi_peminjaman <= 7:
    jenis_pinjaman = "Peminjaman Pendek"
elif 7 < durasi_peminjaman <= 30:
    jenis_pinjaman = "Peminjaman Menengah"
else:
    jenis_pinjaman = "Peminjaman Panjang"

# Menampilkan jenis pinjaman
print(f"Durasi Peminjaman: {durasi_peminjaman} hari")
print(f"Jenis Pinjaman: {jenis_pinjaman}")
