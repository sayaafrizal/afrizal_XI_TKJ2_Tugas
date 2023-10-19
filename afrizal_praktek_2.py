#nama    :afrizal varellino braga
#kelas   :XI TKJ2
#no absen: 1
#soal Buat program Python yang memeriksa apakah suatu file sudah ada di direktori server. Jika file sudah
#ada, program harus mencetak "File sudah ada," jika tidak, program harus mencetak "File belum ada"

# Nama file yang ingin diperiksa
nama_file = input ("Masukkan nama file: ")

# Daftar file yang ada di server
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

# Memeriksa apakah nama_file sudah ada di daftar_file_di_server
if nama_file in daftar_file_di_server:
    print("File sudah ada")
else:
    print("File belum ada")
