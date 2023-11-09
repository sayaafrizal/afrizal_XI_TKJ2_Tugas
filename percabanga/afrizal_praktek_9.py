#nama    :afrizal varellino braga
#kelas   :XI TKJ2
#no absen: 1
#soal Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis
#pinjaman berdasarkan aturan berikut:
#• Peminjaman 7 hari atau kurang: "Peminjaman Pendek"
#• Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah"
#• Peminjaman lebih dari 30 hari: "Peminjaman Panjang"

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
