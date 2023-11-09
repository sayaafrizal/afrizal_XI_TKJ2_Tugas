nilai_investasi = 10000  
target = 20000  
tahun = 0

while nilai_investasi <= target:
    nilai_investasi += nilai_investasi * 0.06  
    tahun += 1

print("Dibutuhkan", tahun, "tahun agar nilai investasi melebihi 20.000 dollar.")