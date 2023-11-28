import random

# Fungsi untuk membuat dan menulis file teks
def buat_file_teks():
    with open('random.txt', 'w') as file:
        for _ in range(100):
            angka = random.randint(1, 399)
            file.write(f"{angka}\n")

# Fungsi untuk membaca file dan menampilkan angka ganjil
def baca_dan_tampilkan_angka_ganjil():
    with open('random.txt', 'r') as file:
        print("Angka Ganjil:")
        for line in file:
            angka = int(line.strip())
            if angka % 2 != 0:
                print(angka)

# Fungsi untuk membaca file dan menampilkan angka genap
def baca_dan_tampikan_angka_genap():
    with open('random.txt', 'r') as file:
        print("Angka Genap:")
        for line in file:
            angka = int(line.strip())
            if angka % 2 == 0:
                print(angka)


# Panggil fungsi untuk membuat file
buat_file_teks()

# Panggil fungsi untuk membaca dan menampilkan angka ganjil
baca_dan_tampilkan_angka_ganjil()

# Panggil fungsi untuk membaca dan menampilkan angka genap
baca_dan_tampikan_angka_genap()
