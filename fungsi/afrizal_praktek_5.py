def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Contoh penggunaan
n_input = int(input("Masukkan nilai n untuk bilangan Fibonacci: "))
hasil_fibonacci = fibonacci(n_input)
print(f"Bilangan Fibonacci ke-{n_input} adalah: {hasil_fibonacci}")