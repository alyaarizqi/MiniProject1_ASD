import os
os.system("cls")
from datetime import datetime

class SistemPesanKue:
    def __init__(self):
        self.pesanan = {}

    def buat_pesanan(self, nama_kue, jenis_kue, harga_kue, topping_kue, ukuran_kue, jumlah_pesanan, nama_pelanggan, tanggal_pemesanan, alamat_pelanggan):
        """Membuat pesanan baru"""
        pesan_id = len(self.pesanan) + 1

        try:
            harga_kue = int(harga_kue)
            jumlah_pesanan = int(jumlah_pesanan)
        except ValueError:
            print("Harga kue dan jumlah pesanan harus dalam bentuk angka.")
            return 

        self.pesanan[pesan_id] = {'nama_kue': nama_kue,
                                'jenis_kue': jenis_kue,
                                'harga_kue': harga_kue,
                                'topping_kue': topping_kue,
                                'ukuran_kue': ukuran_kue,
                                'jumlah_pesanan': jumlah_pesanan,
                                'nama_pelanggan': nama_pelanggan,
                                'tanggal_pemesanan': tanggal_pemesanan,
                                'alamat_pelanggan': alamat_pelanggan}
        print("━━━━━━━━━━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━━━━━━━")
        print(f"Pesanan Anda berhasil dibuat dengan ID {pesan_id}!!")
        print("━━━━━━━━━━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━━━━━━━")

    def baca_pesanan(self, pesan_id):
        """Membaca detail pesanan"""
        if pesan_id in self.pesanan:
            pesan = self.pesanan[pesan_id]
            print("+-------- DETAIL KUE PESANAN --------+")
            print(f"ID Pesanan: {pesan_id}")
            print(f"Nama Kue: {pesan['nama_kue']}")
            print(f"Jenis Kue: {pesan['jenis_kue']}")
            print(f"Harga Kue: {pesan['harga_kue']}")
            print(f"Topping Kue: {pesan['topping_kue']}")
            print(f"Ukuran Kue: {pesan['ukuran_kue']}")
            print(f"Jumlah pesanan: {pesan['jumlah_pesanan']}")
            print(f"Nama Pelanggan: {pesan['nama_pelanggan']}")
            print(f"Alamat Pelanggan: {pesan['alamat_pelanggan']}")
            print(f"Tanggal Pemesanan: {pesan['tanggal_pemesanan']}")
            total_pesanan = self.hitung_totalpesanan(pesan)
            print("━━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━")
            print(f"Total Harga Pesanan: {total_pesanan}")
            print("━━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━")
        else:
            print("━━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━")
            print("  ID Pesanan tidak ditemukan ●__●   ")
            print("━━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━")


    def update_pesanan(self, pesan_id, pilihan):
        """Memperbarui detail pesanan"""
        if pesan_id in self.pesanan:
            print("Pesanan yang tersedia untuk diperbarui:")
            self.baca_pesanan(pesan_id)
            print("+-------- UPDATE DAFTAR KUE PESANAN BARU --------+")
            print("|  Data yang ingin diubah:                       |")
            print("|  1. Nama Kue                                   |")
            print("|  2. Jenis Kue                                  |")
            print("|  3. Harga Kue                                  |")
            print("|  4. Topping Kue                                |")
            print("|  5. Ukuran Kue                                 |")
            print("|  6. Jumlah Pesanan                             |")
            print("|  7. Nama Pelanggan                             |")
            print("|  8. Alamat Pelanggan                           |")
            print("|  9. Keluar                                     |")
            print("+------------------------------------------------+")
            while True:
                pilihan = input("Pilihan Anda: ")
                if pilihan == "1":
                    nama_kue_baru = input("Masukkan Nama Kue (baru): ")
                    self.pesanan[pesan_id]['nama_kue'] = nama_kue_baru
                    print("Nama Kue berhasil diperbarui!")
                elif pilihan == "2":
                    jenis_kue_baru = input("Masukkan Jenis Kue (baru): ")
                    self.pesanan[pesan_id]['jenis_kue'] = jenis_kue_baru
                    print("Jenis Kue berhasil diperbarui!")
                elif pilihan == "3":
                    harga_kue_baru = int(input("Masukkan Harga Kue (baru): "))
                    self.pesanan[pesan_id]['harga_kue'] = harga_kue_baru
                    print("Harga Kue berhasil diperbarui!")
                elif pilihan == "4":
                    topping_kue_baru = input("Masukkan Topping Kue (baru): ")
                    self.pesanan[pesan_id]['topping_kue'] = topping_kue_baru
                    print("Topping Kue berhasil diperbarui!")
                elif pilihan == "5":
                    ukuran_kue_baru = input("Masukkan Ukuran Kue (baru): ")
                    self.pesanan[pesan_id]['ukuran_kue'] = ukuran_kue_baru
                    print("Ukuran Kue berhasil diperbarui!")
                elif pilihan == "6":
                    jumlah_pesanan_baru = int(input("Masukkan Jumlah Pesanan (baru): "))
                    self.pesanan[pesan_id]['jumlah_pesanan'] = jumlah_pesanan_baru
                    print("Jumlah Pesanan berhasil diperbarui!")
                elif pilihan == "7":
                    nama_pelanggan_baru = input("Masukkan Nama Pelanggan (baru): ")
                    self.pesanan[pesan_id]['nama_pelanggan'] = nama_pelanggan_baru
                    print("Nama Pelanggan berhasil diperbarui!")
                elif pilihan == "8":
                    alamat_pelanggan_baru = input("Masukkan Alamat Pelanggan (baru): ")
                    self.pesanan[pesan_id]['alamat_pelanggan'] = alamat_pelanggan_baru
                    print("Alamat Pelanggan berhasil diperbarui!")
                elif pilihan == "9":
                    print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")
                    print("Pembaruan pesanan telah selesai.")
                    print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")
                    self.baca_pesanan(pesan_id)
                    break
                else:
                    print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")
                    print("     Pilihan tidak valid!      ")
                    print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")
        else:
            print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")
            print("  ID Pesanan tidak ditemukan.  ")
            print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")


    def delete_pesanan(self, pesan_id):
        """Menghapus pesanan"""
        if pesan_id in self.pesanan:
            del self.pesanan[pesan_id]
            print("━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━")
            print("Pesanan Anda telah berhasil dihapus!")
            print("━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━")
        else:
            print("━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━")
            print("  ID Pesanan Anda tidak ditemukan.  ")
            print("━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━")

    def hitung_totalpesanan(self, kue):
        """Menghitung total harga kue"""
        total_pesanan = kue["harga_kue"] * kue["jumlah_pesanan"]
        if len(kue["topping_kue"]) > 0:
            total_pesanan += len(kue["topping_kue"]) * 5000  * kue["jumlah_pesanan"]
        return total_pesanan


# Fungsi untuk mengoperasikan CRUD
def operasi_pesan(sistem):
    while True:
        print("===============================")
        print("     SISTEM PEMESANAN KUE      ")
        print("===============================")
        print("+--------Pilih operasi--------+")
        print("|1. Tambah pesanan kue        |")
        print("|2. Lihat pesanan kue         |")
        print("|3. Perbarui pesanan kue      |")
        print("|4. Hapus pesanan kue         |")
        print("|5. Keluar                    |")
        print("+-----------------------------+")
        operasi = input("Pilihan Anda: ")

        if operasi == "1":
            print("+-------- DAFTAR KUE PESANAN --------+")
            nama_kue = input("Masukkan Nama Kue: ")
            print("Pilih jenis kue:")
            print("1. Birthday Cake")
            print("2. Cupcake")
            print("3. Kue Tart")
            print("4. Kue Tradisional")
            print("5. Pastry")
            print("6. Roti")
            jenis_kue = input("Masukkan nomor jenis kue: ")
            while jenis_kue not in ["1", "2", "3", "4", "5", "6"]:
                print("Pilihan tidak valid.")
                jenis_kue = input("Masukkan nomor jenis kue: ")

            if jenis_kue == "1":
                jenis_kue = "Birthday Cake"
            elif jenis_kue == "2":
                jenis_kue = "Cupcake"
            elif jenis_kue == "3":
                jenis_kue = "Kue Tart"
            elif jenis_kue == "4":
                jenis_kue = "Kue Tradisional"
            elif jenis_kue == "5":
                jenis_kue = "Pastry"
            elif jenis_kue == "6":
                jenis_kue = "Roti"
            harga_kue = int(input("Masukkan Harga Kue: "))
            topping_kue = input("Masukkan Topping Kue: ")
            ukuran_kue = input("Masukkan Ukuran Kue: ")
            jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
            nama_pelanggan = input("Masukkan Nama Pelanggan: ")
            tanggal_pemesanan = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            alamat_pelanggan = input("Masukkan Alamat Pelanggan: ")
            sistem.buat_pesanan(nama_kue, jenis_kue, harga_kue, topping_kue, ukuran_kue, jumlah_pesanan, nama_pelanggan, tanggal_pemesanan, alamat_pelanggan)
        elif operasi == "2":
            pesan_id = int(input("Masukkan ID Pesanan yang ingin dilihat: "))
            sistem.baca_pesanan(pesan_id)
        elif operasi == "3":
            pesan_id = int(input("Masukkan ID Pesanan yang ingin diperbarui: "))
            sistem.baca_pesanan(pesan_id)
            print("+-------- UPDATE DAFTAR KUE PESANAN BARU --------+")
            print("Pilih data yang ingin diperbarui:")
            print("1. Nama Kue")
            print("2. Jenis Kue")
            print("3. Harga Kue")
            print("4. Topping Kue")
            print("5. Ukuran Kue")
            print("6. Jumlah Pesanan")
            print("7. Nama Pelanggan")
            print("8. Alamat Pelanggan")
            pilihan = input("Pilihan Anda: ")
            sistem.update_pesanan(pesan_id, pilihan)
        elif operasi == "4":
            pesan_id = int(input("Masukkan ID Pesanan yang ingin dihapus: "))
            sistem.delete_pesanan(pesan_id)
            if not sistem.pesanan:  # Jika daftar pesanan kosong
                print("Tidak ada pesanan yang tersedia untuk diperbarui.")
                continue
        elif operasi == "5":
            print("━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━")
            print(" Terima kasih telah berbelanja !!!  ")
            print("━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━")
            break
        else:
            print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━")
            print("   Pilihan Anda tidak valid!     ")
            print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━")


# Contoh penggunaan:
sistem_pemesanan = SistemPesanKue()
operasi_pesan(sistem_pemesanan)