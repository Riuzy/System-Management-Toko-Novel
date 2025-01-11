from login import login
from menu.menu_admin import menu_admin

def main():
    print("Sistem Manajemen Toko Novel")
    while True:
        print("1. Login Admin")
        print("2. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            login()
            menu_admin()
        elif choice == "2":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
