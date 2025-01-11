from datetime import datetime

class Novel:
    def __init__(self, judul, penulis, genre, tahun_rilis, stok, harga):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        self.tahun_rilis = tahun_rilis
        self.stok = stok
        self.harga = harga

    def to_dict(self):
        return {
            "judul": self.judul,
            "penulis": self.penulis,
            "genre": self.genre,
            "tahun_rilis": self.tahun_rilis,
            "stok": self.stok,
            "harga": self.harga,
        }

class Pembeli:
    def __init__(self, nama, alamat, no_tlp, judul, jumlah, harga_per_unit, tanggal_transaksi=None):
        self.nama = nama
        self.alamat = alamat
        self.no_tlp = no_tlp
        self.judul = judul
        self.jumlah = jumlah
        self.harga_per_unit = harga_per_unit
        self.total_harga = jumlah * harga_per_unit
        self.tanggal_transaksi = tanggal_transaksi or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "nama": self.nama,
            "alamat": self.alamat,
            "no_tlp": self.no_tlp,
            "judul": self.judul,
            "jumlah": self.jumlah,
            "harga_per_unit": self.harga_per_unit,
            "total_harga": self.total_harga,
            "tanggal_transaksi": self.tanggal_transaksi
        }
