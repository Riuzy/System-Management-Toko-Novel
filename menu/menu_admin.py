from datetime import datetime
import json
from struktur.liststack import Novel_Stack
from struktur.listqueue import Pembeli_Queue
from struktur.search import binary_search
from struktur.sort import insertion_sort
from struktur.struct import Pembeli, Novel
from prettytable import PrettyTable

novel_stack = Novel_Stack()
pembeli_queue = Pembeli_Queue()

def display_table(data_list, headers):
    table = PrettyTable()
    table.field_names = headers
    for data in data_list:
        table.add_row([data.get(key, "") for key in headers])
    print(table)

def menu_admin():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Tambah Novel Baru")
        print("2. Tampilkan List Novel")
        print("3. Edit Novel")
        print("4. Hapus Novel")
        print("5. Masukkan Transaksi")
        print("6. Lihat Riwayat Transaksi")
        print("7. Urutkan Novel")
        print("8. Cari Novel atau Riwayat Transaksi")
        print("9. Kembali ke menu login")
        choice = input("Pilih menu: ")

        if choice == "1":
            judul = input("Masukkan judul: ")
            penulis = input("Masukkan penulis: ")
            genre = input("Masukkan genre: ")
            tahun_rilis = int(input("Masukkan tahun rilis: "))
            stok = int(input("Masukkan stok: "))
            harga = int(input("Masukkan harga: "))
            novel_stack.push_novel(Novel(judul, penulis, genre, tahun_rilis, stok, harga))
            print("Novel berhasil Ditambahkan.")

        elif choice == "2":
            novels = novel_stack.display()
            print("\nDaftar Novel:")
            if novels:
                display_table(novels, ["judul", "penulis", "genre", "tahun_rilis", "stok", "harga"])
            else:
                print("Tidak ada novel yang tersedia.")
                
        elif choice == "3":
            judul_edit = input("Masukkan judul novel yang ingin diedit: ")


            try:
                with open(novel_stack.file_path, "r") as file:
                    novels = json.load(file)
            except FileNotFoundError:
                novels = []

            novel_to_edit = None
            for novel in novels:
                if novel["judul"].lower() == judul_edit.lower():
                    novel_to_edit = novel
                    break 

            if novel_to_edit:
                print("Novel ditemukan. Masukkan data baru (kosongkan jika tidak ingin mengubah):")
                penulis = input(f"Penulis [{novel_to_edit['penulis']}]: ") or novel_to_edit["penulis"]
                genre = input(f"Genre [{novel_to_edit['genre']}]: ") or novel_to_edit["genre"]
                tahun_rilis = input(f"Tahun Rilis [{novel_to_edit['tahun_rilis']}]: ") or novel_to_edit["tahun_rilis"]
                stok = input(f"Stok [{novel_to_edit['stok']}]: ") or novel_to_edit["stok"]
                harga = input(f"Harga [{novel_to_edit['harga']}]: ") or novel_to_edit["harga"]

                for novel in novels:
                    if novel["judul"].lower() == judul_edit.lower():
                        novel.update({
                            "judul": judul_edit,
                            "penulis": penulis,
                            "genre": genre,
                            "tahun_rilis": int(tahun_rilis),
                            "stok": int(stok),
                            "harga": int(harga)
                        })

                with open(novel_stack.file_path, "w") as file:
                    json.dump(novels, file, indent=4)

                print("Novel berhasil diperbarui.")
            else:
                print("Novel tidak ditemukan.")

        elif choice == "4":
            judul_hapus = input("Masukkan judul novel yang ingin dihapus: ")

            try:
                with open(novel_stack.file_path, "r") as file:
                    novels = json.load(file)
            except FileNotFoundError:
                novels = []
            updated_novels = [novel for novel in novels if novel["judul"].lower() != judul_hapus.lower()]

            if len(updated_novels) < len(novels): 
                with open(novel_stack.file_path, "w") as file:
                    json.dump(updated_novels, file, indent=4)
                print(f"Novel '{judul_hapus}' berhasil dihapus.")
            else:
                print(f"Novel '{judul_hapus}' tidak ditemukan.")
        elif choice == "5":
            nama = input("Masukkan nama pembeli: ")
            alamat = input("Masukkan alamat pembeli: ")
            no_tlp = input("Masukkan nomor telepon pembeli: ")
            judul_beli = input("Masukkan judul novel yang dibeli: ")
            jumlah = int(input("Masukkan jumlah pembelian: "))

            novels = novel_stack.display()
            novel = next((n for n in novels if n['judul'].lower() == judul_beli.lower()), None)

            if novel and novel['stok'] >= jumlah:
                novel['stok'] -= jumlah
                novel_stack.top = None  
                for n in novels:
                    novel_stack.push_novel(Novel(**n)) 
                pembeli_queue.enqueue(
                    Pembeli(
                        nama=nama,
                        alamat=alamat,
                        no_tlp=no_tlp,
                        judul=judul_beli,
                        jumlah=jumlah,
                        harga_per_unit=novel['harga'],
                        tanggal_transaksi=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
                )
                print(f"Transaksi berhasil! Anda membeli {jumlah} buku '{judul_beli}'.")
            else:
                print("Novel tidak tersedia atau stok tidak mencukupi.")


        elif choice == "6":
            pembeli_list = pembeli_queue.display()
            print("\nRiwayat Pembelian:")
            if pembeli_list:
                display_table(
                    pembeli_list,
                    ["nama", "alamat", "no_tlp", "judul", "jumlah", "total_harga", "tanggal_transaksi"]
                )
            else:
                print("Belum ada riwayat pembelian.")

        elif choice == "7":
            order = input("Urutkan berdasarkan: (judul/tahun_rilis/harga): ")
            asc_desc = input("Urutkan (asc/desc): ")
            ascending = True if asc_desc.lower() == "asc" else False
            novels = novel_stack.display()
            sorted_novels = insertion_sort(novels, key=order, ascending=ascending)
            print("\nNovel Setelah Diurutkan:")
            if sorted_novels:
                display_table(sorted_novels, ["judul", "penulis", "genre", "tahun_rilis", "stok", "harga"])
            else:
                print("Tidak ada novel untuk diurutkan.")

        elif choice == "8":
            category = input("Cari di (novel/pembelian): ").strip().lower()
            key = input("Cari berdasarkan (judul/nama): ").strip().lower()
            value = input("Masukkan nilai pencarian: ").strip()
            
            if category == "novel":
                novels = novel_stack.display()
                novels = sorted(novels, key=lambda x: str(x.get(key, "")).strip().lower())
                result = binary_search(novels, key, value)
                if result:
                    print("Hasil Pencarian Novel:")
                    display_table([result], ["judul", "penulis", "genre", "tahun_rilis", "stok", "harga"])
                else:
                    print("Novel tidak ditemukan.")
            
            elif category == "pembelian":
                pembeli_list = pembeli_queue.display()
                pembeli_list = sorted(pembeli_list, key=lambda x: str(x.get(key, "")).strip().lower())
                result = binary_search(pembeli_list, key, value) 
                if result:
                    print("Hasil Pencarian Pembelian:")
                    display_table([result], ["nama", "alamat", "no_tlp", "judul", "jumlah", "total_harga", "tanggal_transaksi"])
                else:
                    print("Riwayat pembelian tidak ditemukan.")

        elif choice == "9":
            break
        else:
            print("Pilihan tidak valid.")
