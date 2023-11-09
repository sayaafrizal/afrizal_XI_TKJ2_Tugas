def hitung_pangkat(bilangan, eksponen):
    return bilangan ** eksponen

# Contoh penggunaan
bilangan_input = float(input("Masukkan bilangan: "))
eksponen_input = int(input("Masukkan eksponen: "))
hasil_pangkat = hitung_pangkat(bilangan_input, eksponen_input)
print(f"Hasil {bilangan_input}^{eksponen_input} adalah: {hasil_pangkat}")