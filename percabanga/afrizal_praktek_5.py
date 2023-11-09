#nama    :afrizal varellino braga
#kelas   :XI TKJ2
#no absen: 1
#soal Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori
#produk berdasarkan penjualan:
#• Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris."
#• Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer."
#• Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."

penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))

# Menentukan kategori produk berdasarkan aturan yang diberikan
if penjualan > 1000:
    kategori = "Produk Terlaris"
elif 500 <= penjualan <= 1000:
    kategori = "Produk Populer"
else:
    kategori = "Produk Biasa"

# Menampilkan kategori produk
print(f"Jumlah Penjualan: {penjualan} unit")
print(f"Kategori Produk: {kategori}")
