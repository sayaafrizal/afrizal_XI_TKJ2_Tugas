#nama    :afrizal varellino braga
#kelas   :XI TKJ2
#no absen: 1
#soal Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukan
#apakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, program harus mencetak
#"Sistem perlu di-restart." Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."
# Meminta input informasi pembaruan (misalnya: "Y" atau "N")
pembaruan = input("Apakah terdapat pembaruan yang memerlukan restart (Y/N)? ").strip().lower()

# Memeriksa apakah pembaruan memerlukan restart
if pembaruan == "y":
    print("Sistem perlu di-restart.")
elif pembaruan == "n":
    print("Sistem tidak perlu di-restart.")
else:
    print("Input tidak valid. Silakan masukkan 'Y' atau 'N' untuk mengindikasikan pembaruan.")
