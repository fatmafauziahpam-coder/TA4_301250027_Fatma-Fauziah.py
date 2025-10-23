# pola_piramida_terbalik.py
def inverted_pyramid(n):
    """
    Cetak pola piramida terbalik sebanyak n baris.
    Baris pertama memiliki n bintang, lalu berkurang 1 tiap baris.
    """
    for i in range(n, 0, -1):
        print('*' * i)

if __name__ == "__main__":
    try:
        n = int(input("Masukkan tinggi piramid (mis. 5): ").strip())
        if n <= 0:
            print("Masukkan angka positif lebih besar dari 0.")
        else:
            inverted_pyramid(n)
    except ValueError:
        print("Input tidak valid. Masukkan bilangan bulat.")


# Program: Simulasi Login (maksimal 3 kali percobaan)

# Username dan password yang benar
username_benar = "admin"
password_benar = "python"

# Jumlah percobaan maksimal
maks_percobaan = 3

# Perulangan login
for percobaan in range(1, maks_percobaan + 1):
    print(f"Percobaan ke-{percobaan}")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username == username_benar and password == password_benar:
        print("Login berhasil! Selamat datang,", username)
        break
    else:
        sisa = maks_percobaan - percobaan
        if sisa > 0:
            print(f"Username atau password salah. Sisa percobaan: {sisa}\n")
        else:
            print("Akun diblokir! Anda telah gagal login sebanyak 3 kali.")