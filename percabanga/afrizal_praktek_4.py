#nama    :afrizal varellino braga
#kelas   :XI TKJ2
#no absen: 1
#soal Buat program Python yang mengambil nilai tugas (skala 0-100) dan nilai ujian (skala 0-100) seorang
#siswa dan menentukan nilai akhirnya. Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswa
#lulus dengan nilai "Lulus". Jika tidak, siswa gagal dengan nilai "Gagal".

nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))

# Menentukan apakah siswa lulus atau tidak berdasarkan aturan yang diberikan
if nilai_tugas > 70 and nilai_ujian > 60:
    status = "Lulus"
else:
    status = "Gagal"

# Menampilkan nilai akhir dan status siswa
print(f"Nilai Tugas: {nilai_tugas}")
print(f"Nilai Ujian: {nilai_ujian}")
print(f"Status: {status}")
