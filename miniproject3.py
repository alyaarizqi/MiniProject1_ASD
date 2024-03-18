import os
os.system("cls")
from datetime import datetime

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SistemPesanKue:
    def __init__(self):
        self.head = None
        self.pesanan = None 


    def sorting_pesanan(self, key1, key2, ascending=True):
        pesanan_list = []
        current = self.head
        while current:
            pesanan_list.append(current.data)
            current = current.next

        if ascending:
            pesanan_list.sort(key=lambda x: (x.get(key1), x.get(key2)))
        else:
            pesanan_list.sort(key=lambda x: (x.get(key1), x.get(key2)), reverse=True)

        self.head = None
        for pesanan in pesanan_list:
            if not self.head:
                self.head = Node(pesanan)
            else:
                self.tambah_di_akhir(pesanan)


    #implementasi tambahan untuk sorting dengan menggunakan Quick Sort
    def quick_sort(self, data, key, ascending=True):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0].get(key)  

            less_than_pivot = [x for x in data[1:] if x.get(key) is not None and x.get(key) <= pivot]
            greater_than_pivot = [x for x in data[1:] if x.get(key) is not None and x.get(key) > pivot]

        if ascending:
            return self.quick_sort(less_than_pivot, key, ascending) + [data[0]] + self.quick_sort(greater_than_pivot, key, ascending)
        else:
            return self.quick_sort(greater_than_pivot, key, ascending) + [data[0]] + self.quick_sort(less_than_pivot, key, ascending)
        
    def tambah_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def tambah_di_tengah(self, prev_node, data):
        if not prev_node:
            print("Node sebelumnya tidak ditemukan.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def hapus_di_awal(self):
        if not self.head:
            print("Linked list kosong.")
            return
        self.head = self.head.next

    def hapus_di_akhir(self):
        if not self.head:
            print("Linked list kosong.")
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def hapus_di_tengah(self, prev_node):
        if not prev_node or not prev_node.next:
            print("Node sebelumnya tidak ditemukan.")
            return
        prev_node.next = prev_node.next.next

    def tampilkan(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def buat_pesanan(self, nama_kue, jenis_kue, harga_kue, topping_kue, ukuran_kue, jumlah_pesanan, nama_pelanggan, tanggal_pemesanan, alamat_pelanggan):
        """Membuat pesanan baru"""
        try:
            self.pesanan_hitung += 1
        except AttributeError:
            self.pesanan_hitung = 1

        pesan_id = self.pesanan_hitung

        try:
            harga_kue = int(harga_kue)
            jumlah_pesanan = int(jumlah_pesanan)
        except ValueError:
            print("Harga kue dan jumlah pesanan harus dalam bentuk angka.")
            return 

        print("Menu Tambah Pesanan:")
        print("1. Tambah di Awal")
        print("2. Tambah di Akhir")
        print("3. Tambah di Tengah")

        pilihan = input("Pilih tempat penambahan pesanan: ")

        if pilihan not in ["1", "2", "3"]:
            print("Pilihan tidak valid. Pesanan tidak ditambahkan.")
            return

        if pilihan == "1":
            self.tambah_di_awal({
                'id': pesan_id,
                'nama_kue': nama_kue,
                'jenis_kue': jenis_kue,
                'harga_kue': harga_kue,
                'topping_kue': topping_kue,
                'ukuran_kue': ukuran_kue,
                'jumlah_pesanan': jumlah_pesanan,
                'nama_pelanggan': nama_pelanggan,
                'tanggal_pemesanan': tanggal_pemesanan,
                'alamat_pelanggan': alamat_pelanggan
            })
        elif pilihan == "2":
            self.tambah_di_akhir({
                'id': pesan_id,
                'nama_kue': nama_kue,
                'jenis_kue': jenis_kue,
                'harga_kue': harga_kue,
                'topping_kue': topping_kue,
                'ukuran_kue': ukuran_kue,
                'jumlah_pesanan': jumlah_pesanan,
                'nama_pelanggan': nama_pelanggan,
                'tanggal_pemesanan': tanggal_pemesanan,
                'alamat_pelanggan': alamat_pelanggan
            })
        elif pilihan == "3":
            current = self.head
            count = 1
            while current:
                current = current.next
                count += 1
            posisi_tengah = count // 2  
            current = self.head
            for _ in range(posisi_tengah - 1):
                current = current.next
            self.tambah_di_tengah(current, {
                'id': pesan_id,
                'nama_kue': nama_kue,
                'jenis_kue': jenis_kue,
                'harga_kue': harga_kue,
                'topping_kue': topping_kue,
                'ukuran_kue': ukuran_kue,
                'jumlah_pesanan': jumlah_pesanan,
                'nama_pelanggan': nama_pelanggan,
                'tanggal_pemesanan': tanggal_pemesanan,
                'alamat_pelanggan': alamat_pelanggan
            })

        print("━━━━━━━━━━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━━━━━━━")
        print(f"Pesanan Anda berhasil dibuat dengan ID {pesan_id}!!")
        print("━━━━━━━━━━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━━━━━━━")


    def baca_pesanan(self, pesan_id=None):
        """Menampilkan semua pesanan"""
        if not self.head:
            print("Tidak ada pesanan yang tersedia saat ini.")
            os.system("pause")
            return

        current = self.head
        while current:
            pesan = current.data
            if pesan_id is None or pesan['id'] == pesan_id:
                print("+-------- DETAIL KUE PESANAN --------+")
                print(f"ID Pesanan: {pesan['id']}")
                print(f"Nama Kue: {pesan['nama_kue']}")
                print(f"Jenis Kue: {pesan['jenis_kue']}")
                print(f"Harga Kue: {pesan['harga_kue']}")
                print(f"Topping Kue: {pesan['topping_kue']}")
                print(f"Ukuran Kue: {pesan['ukuran_kue']}")
                print(f"Jumlah pesanan: {pesan['jumlah_pesanan']}")
                print(f"Nama Pelanggan: {pesan['nama_pelanggan']}")
                print(f"Alamat Pelanggan: {pesan['alamat_pelanggan']}")
                print(f"Tanggal Pemesanan: {pesan['tanggal_pemesanan']}")
                total_pesanan = self.hitung_total_pesanan(pesan)
                print("━━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━")
                print(f"Total Harga Pesanan: {total_pesanan}")
                print("━━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━")
            current = current.next
        os.system("pause")

    def update_pesanan(self, pesan_id, pilihan):
        """Memperbarui detail pesanan"""
        current = self.head
        while current:
            if current.data['id'] == pesan_id:
                print("Pesanan yang tersedia untuk diperbarui:")
                self.baca_pesanan(pesan_id)
                pesan = current.data
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
                        pesan['nama_kue'] = nama_kue_baru
                        print("Nama Kue berhasil diperbarui!")
                    elif pilihan == "2":
                        jenis_kue_baru = input("Masukkan Jenis Kue (baru): ")
                        pesan['jenis_kue'] = jenis_kue_baru
                        print("Jenis Kue berhasil diperbarui!")
                    elif pilihan == "3":
                        harga_kue_baru = int(input("Masukkan Harga Kue (baru): "))
                        pesan['harga_kue'] = harga_kue_baru
                        print("Harga Kue berhasil diperbarui!")
                    elif pilihan == "4":
                        topping_kue_baru = input("Masukkan Topping Kue (baru): ")
                        pesan['topping_kue'] = topping_kue_baru
                        print("Topping Kue berhasil diperbarui!")
                    elif pilihan == "5":
                        ukuran_kue_baru = input("Masukkan Ukuran Kue (baru): ")
                        pesan['ukuran_kue'] = ukuran_kue_baru
                        print("Ukuran Kue berhasil diperbarui!")
                    elif pilihan == "6":
                        jumlah_pesanan_baru = int(input("Masukkan Jumlah Pesanan (baru): "))
                        pesan['jumlah_pesanan'] = jumlah_pesanan_baru
                        print("Jumlah Pesanan berhasil diperbarui!")
                    elif pilihan == "7":
                        nama_pelanggan_baru = input("Masukkan Nama Pelanggan (baru): ")
                        pesan['nama_pelanggan'] = nama_pelanggan_baru
                        print("Nama Pelanggan berhasil diperbarui!")
                    elif pilihan == "8":
                        alamat_pelanggan_baru = input("Masukkan Alamat Pelanggan (baru): ")
                        pesan['alamat_pelanggan'] = alamat_pelanggan_baru
                        print("Alamat Pelanggan berhasil diperbarui!")
                    elif pilihan == "9":
                        print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")
                        print("Pembaruan pesanan telah selesai.")
                        print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")
                        self.baca_pesanan()  # Pass pesan_id di sini
                        break
                    else:
                        print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")
                        print("     Pilihan tidak valid!      ")
                        print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")
                return
            current = current.next
        print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")
        print("  ID Pesanan tidak ditemukan.  ")
        print("━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━")

    def hapus_pesanan(self, pesan_id):
        """Menghapus pesanan"""
        current = self.head
        prev_node = None
        while current:
            if current.data['id'] == pesan_id:
                if prev_node:
                    prev_node.next = current.next
                else:
                    self.head = current.next
                print("━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━")
                print("Pesanan Anda telah berhasil dihapus!")
                print("━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━")
                return
            prev_node = current
            current = current.next
        print("━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━")
        print("  ID Pesanan Anda tidak ditemukan.  ")
        print("━━━━━━━━━━━━━━━ ⋆⋅☆⋅⋆ ━━━━━━━━━━━━━━━")


    def hitung_total_pesanan(self, kue):
        """Menghitung total harga kue"""
        total_pesanan = kue["harga_kue"] * kue["jumlah_pesanan"]
        if len(kue["topping_kue"]) > 0:
            total_pesanan += len(kue["topping_kue"]) * 5000  * kue["jumlah_pesanan"]
        return total_pesanan

    def operasi_pesan(self):
        while True:
            print("=================================")
            print("     SISTEM PEMESANAN KUE        ")
            print("=================================")
            print("+--------Pilih operasi----------+")
            print("|1. Tambah pesanan kue          |")
            print("|2. Lihat pesanan kue           |")
            print("|3. Perbarui pesanan kue        |")
            print("|4. Hapus pesanan kue           |")
            print("|5. Sorting pesanan             |")
            print("|6. Keluar                      |")
            print("+-------------------------------+")
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
                self.buat_pesanan(nama_kue, jenis_kue, harga_kue, topping_kue, ukuran_kue, jumlah_pesanan, nama_pelanggan, tanggal_pemesanan, alamat_pelanggan)
            elif operasi == "2":
                self.baca_pesanan()
            elif operasi == "3":
                pesan_id = int(input("Masukkan ID Pesanan yang ingin diperbarui: "))
                self.baca_pesanan()  
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
                self.update_pesanan(pesan_id, pilihan)
            elif operasi == "4":
                print("+-------- HAPUS DAFTAR KUE PESANAN --------+")
                pesan_id = int(input("Masukkan ID Pesanan yang ingin dihapus: "))
                print("1. Hapus di Awal")
                print("2. Hapus di Akhir")
                print("3. Hapus di Tengah")
                pilihan_hapus = input("Pilih tempat penghapusan pesanan: ")
                if pilihan_hapus not in ["1", "2", "3"]:
                    print("Pilihan tidak valid. Penghapusan pesanan dibatalkan.")
                    continue
                if pilihan_hapus == "1":
                    sistem_pemesanan.hapus_di_awal()
                elif pilihan_hapus == "2":
                    sistem_pemesanan.hapus_di_akhir()
                elif pilihan_hapus == "3":
                    prev_node = None
                    current = sistem_pemesanan.head
                    while current:
                        if current.data['id'] == pesan_id:
                            break
                        prev_node = current
                        current = current.next
                    sistem_pemesanan.hapus_di_tengah(prev_node)
                print("Pesanan telah dihapus.")
            elif operasi == "5":
                print("Pilih operasi untuk melakukan sorting:")
                print("1. Nama Kue")
                print("2. Jenis Kue")
                operasi = input("Pilihan Anda: ")

                if operasi == "1":
                    operasi = 'nama_kue'
                elif operasi == "2":
                    operasi = 'jenis_kue'
                else:
                    print("Pilihan anda tidak valid!!!")
                    continue

                print("Pilih jenis sorting:")
                print("1. Ascending")
                print("2. Descending")
                sorting = input("Pilihan Anda: ")

                ascending = sorting == "1"
                if sorting == "2":
                    self.sorting_pesanan(operasi, 'id', ascending=False)  # Tambahkan 'id' sebagai key2
                else:
                    self.sorting_pesanan(operasi, 'id', ascending)  # Tambahkan 'id' sebagai key2
                self.baca_pesanan()
                
            elif operasi == "6":
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
sistem_pemesanan.operasi_pesan()