import os
import time
import pwinput
from prettytable import PrettyTable

User = {
    "admin": {"password": "admin123", "status": "admin"},
    "user1": {"password": "user123", "status": "user"},
}

Antrean = {
    "KT 1234AB": {"nama": "Carmen", "jenis_motor": "mio", "jenis_cucian": "cuci premium"},
    "KT 6789CD": {"nama": "Ian", "jenis_motor": "Beat", "jenis_cucian": "biasa"}
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def lihat_antrean():
    
    print("\n--- daftar antrean ---")
    if Antrean == {}:
        print("antrean masih kosong.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["plat motor", "nama pemilik", "jenis motor", "jenis cucian"]
        for plat, data in Antrean.items():
            tabel.add_row([plat, data["nama"], data["jenis_motor"], data["jenis_cucian"]])
        print(tabel)

def tambah_antrean():
    
    print("\n--- tambah antrean ---")
    plat = input("Plat motor: ")

    if plat == "":
        print("plat motor tidak boleh kosong!")
        return

    if plat in Antrean:
        print("plat motor sudah terdaftar!")
        return

    nama = input("nama pemilik: ")
    jenis_motor = input("jenis motor: ")
    jenis_cucian = input("jenis_cucian: ")

    Antrean[plat] = {
        "nama": nama, 
        "jenis_motor": jenis_motor,
        "jenis_cucian": jenis_cucian
    }

    print("antrean berhasil ditambahkan!")
    print("data:", plat, Antrean[plat])

def ubah_antrean():
    
    print("\n--- ubah data ---")
    plat = input("masukkan plat motor yang ingin di ubah: ")

    if plat in Antrean:
        print("data ditemukan:", plat, Antrean[plat])

        nama = input("nama pemilik baru: ")
        jenis_motor = input("jenis motor baru: ")
        jenis_cucian = input("jenis cucian baru: ")

        Antrean[plat] = {
            "nama": nama,
            "jenis_motor": jenis_motor,
            "jenis_cucian": jenis_cucian
        }

        print("data berhasil diubah!")
        print("data terbaru:", plat, Antrean[plat])
    else:
        print("plat motor tidak ditemukan")

def hapus_antrean():
    
    print("\n--- hapus antrean ---")
    plat = input("masuk plat motor yang ingin dihapus: ")

    if plat in Antrean:
        del Antrean[plat]
        print("antrean berhasil dihapus:", plat)
    else:
        print("plat motor tidak ditemukan.")

def login():
    
    print("=== Login Sistem Antrean ===")
    username = input("username: ")
    password = pwinput.pwinput("password: ")

    if username in User and User [username] ["password"] == password:
        status= User[username]["status"]
        print(f"\nlogin berhasil! Selamat datang {username} ({status})")
        time.sleep(3)
        return status
    else:
        print("\n username atau password salah!")
        time.sleep(3)
        return None

def menu_utama():
    clear()
    status = None
    while status == None:
        status = login()

    while True:
        
        print("\n=== manajemen antrean cuci motor ===")
        print(f"Status pengguna: {status}")

        if status == "admin":
            print("1. tambah antrean")
            print("2. lihat antrean")
            print("3. ubah data")
            print("4. hapus antrean")
            print("5. keluar program")
            pilihan = input("pilih menu: ")

            if pilihan == "1":
                tambah_antrean()
                input("\n Tekan Enter untuk melanjutkan...")
            elif pilihan == "2":
                lihat_antrean()
                input("\n Tekan Enter untuk melanjutkan...")
            elif pilihan == "3":
                ubah_antrean()
                input("\n Tekan Enter untuk melanjutkan...")
            elif pilihan == "4":
                hapus_antrean()
                input("\n Tekan Enter untuk melanjutkan...")
            elif pilihan == "5":
                print("\n program selesai. Terima Kasih!")
                break
            else:
                print("menu tidak tersedia!")
                print("silahkan pilih menu 1-5.")

        elif status == "user":
            print("1. lihat antrean")
            print("2. keluar program")
            pilihan = input("pilih menu: ")

            if pilihan == "1":
                lihat_antrean()
                input("\n Tekan Enter untuk melanjutkan...")

            elif pilihan == "2":
                print("\n program selesai. Terima Kasih!")
                break

            else:
                print("menu tidak tersedia!")
                print("silahkan pilih menu 1-3.")
                time.sleep(3)

menu_utama()











