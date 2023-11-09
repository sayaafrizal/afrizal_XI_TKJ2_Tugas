#nama    :afrizal varellino braga
#kelas   :XI TKJ2
#no absen: 1
#soal Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai
#performa terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut:
#• Performa 5: Bonus 20% dari gaji tahunan.
#• Performa 4: Bonus 10% dari gaji tahunan.
#• Performa 3: Bonus 5% dari gaji tahunan.
#• Performa 2: Bonus 2% dari gaji tahunan.
#• Performa 1: Tidak ada bonus.
#Buatlah program menggunakan percabangan ternary untuk menghitung bonus tersebut.

#  Meminta input nilai performa karyawan (1-5)
performa = int(input("Masukkan nilai performa karyawan (1-5): "))

# Meminta input gaji tahunan karyawan
gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

# Menghitung bonus tahunan menggunakan percabangan ternary
bonus = (0.20 * gaji_tahunan) if performa == 5 else \
        (0.10 * gaji_tahunan) if performa == 4 else \
        (0.05 * gaji_tahunan) if performa == 3 else \
        (0.02 * gaji_tahunan) if performa == 2 else 0

# Menampilkan bonus tahunan
print(f"Bonus Tahunan: {bonus:.2f} IDR")
