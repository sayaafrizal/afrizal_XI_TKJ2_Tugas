# Meminta input status persiapan proyek (Siap atau Tunda)
status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ").strip().lower()

# Menentukan apakah proyek dapat diluncurkan
if status_persiapan == "siap":
    print("Proyek diluncurkan.")
elif status_persiapan == "tunda":
    print("Proyek ditunda.")
else:
    print("Status persiapan tidak valid. Masukkan 'Siap' atau 'Tunda'.")
