import random

def tebak_angka():
    print("=== Game Tebak Angka ===")
    print("Saya sudah memilih angka antara 1 sampai 100.")
    print("Coba tebak angka tersebut!")
    
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    percobaan = 0
    
    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Masukkan tebakanmu: "))
            percobaan += 1
            
            if tebakan < angka_rahasia:
                print("Terlalu kecil, coba lagi!")
            elif tebakan > angka_rahasia:
                print("Terlalu besar, coba lagi!")
            else:
                print(f"Selamat! Kamu berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
        except ValueError:
            print("Masukkan angka yang valid!")

tebak_angka()
