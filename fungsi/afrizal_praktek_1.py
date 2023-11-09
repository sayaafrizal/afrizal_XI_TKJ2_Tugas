#nama=afrizal vb
#kelas=XI tkj2
#soal=Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna.
#Rumus: Total deret bilangan ganjil = 1 + 3 + 5 + ... + (2n-1)
def total_deret_ganjil(batas):
    total = 0
    for i in range(1, 2*batas, 2):
        total += i
    return total

# Contoh penggunaan
batas_pengguna = int(input("Masukkan batas deret ganjil: "))
hasil_total = total_deret_ganjil(batas_pengguna)
print(f"Total deret bilangan ganjil hingga batas {batas_pengguna} adalah: {hasil_total}")