jumlah_apel = 100  
batas_sisa_apel = 20  
hari = 0

while jumlah_apel > batas_sisa_apel:
    jumlah_apel -= jumlah_apel * 0.10  
    hari += 1

print("Dibutuhkan", hari, "hari agar sisa apel kurang dari 20 buah.")