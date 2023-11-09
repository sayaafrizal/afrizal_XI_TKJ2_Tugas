jumlah_ayam = 100 
target = 200  
bulan = 0

while jumlah_ayam <= target:
    jumlah_ayam += jumlah_ayam * 0.05 
    bulan += 1

print("Dibutuhkan", bulan, "bulan agar jumlah ayam melebihi 200 ekor.")
