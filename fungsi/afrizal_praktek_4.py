def jumlah_digit(bilangan):
    return sum(int(digit) for digit in str(bilangan))

# Contoh penggunaan
bilangan_input = int(input("Masukkan bilangan: "))
hasil_jumlah_digit = jumlah_digit(bilangan_input)
print(f"Jumlah digit dari {bilangan_input} adalah: {hasil_jumlah_digit}")