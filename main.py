import os
from randomId import random_id
from list_barang import list_barang as lb
import crud
insert_data = crud.insert_data

def proses_sewa():
    data_sewaan = []
    qty_sewaan = []                         #LIST KOSONG U/ MENYIMPAN DATA SEWAAN

    def clear_screen():                                                # CEK SISTEM OPERASI
        sistem_operasi = os.name

        if sistem_operasi == 'posix':
            os.system('clear')
        elif sistem_operasi == 'nt' :
            os.system('cls')

    print('\n\n')
    print('-'*60)
    print('='*5, 'SELAMAT DATANG DI PROGRAM PENYEWAAN ALAT OUTDOOR', '='*5)
    print('-'*60)

    def pilih_barang_disewa():
        id_pesanan = int(input('Masukkan id barang disewa : '))
        if id_pesanan == 1:
            input_id = 1
            input_nama_brg = 'Tenda dome max 4 org'
            input_harga_brg = 20000
        elif id_pesanan == 2:
            input_id = 2
            input_nama_brg = 'Tenda Consina Magnum 4'
            input_harga_brg = 30000
        elif id_pesanan == 3:
            input_id = 3
            input_nama_brg = 'Tenda Pramuka 10 org'
            input_harga_brg = 50000
        elif id_pesanan == 4:
            input_id = 4
            input_nama_brg = 'Carrier + Cover 60 & 80 lt'
            input_harga_brg = 15000
        elif id_pesanan == 5:
            input_id = 5
            input_nama_brg = 'Carrier REI / Consina 60 lt + Cover'
            input_harga_brg = 20000
        elif id_pesanan == 6:
            input_id = 6
            input_nama_brg = 'Carrier REI 80 lt + Cover'
            input_harga_brg = 25000
        elif id_pesanan == 7:
            input_id = 7
            input_nama_brg = 'Sleeping Bag (Dacron/Pollar)'
            input_harga_brg = 5000
        elif id_pesanan == 8:
            input_id = 8
            input_nama_brg = 'Nesting TNI'
            input_harga_brg = 5000
        elif id_pesanan == 9:
            input_id = 9
            input_nama_brg = 'Kompor Gasmate'
            input_harga_brg = 5000
        elif id_pesanan == 10:
            input_id = 10
            input_nama_brg = 'Lentera Tenda (LED)'
            input_harga_brg = 5000
        elif id_pesanan == 11:
            input_id = 11
            input_nama_brg = 'Headlamp (LED)'
            input_harga_brg = 5000
        elif id_pesanan == 12:
            input_id = 12
            input_nama_brg = 'Flysheet'
            input_harga_brg = 6000
        elif id_pesanan == 13:
            input_id = 13
            input_nama_brg = 'Eggholder isi 12'
            input_harga_brg = 5000
        elif id_pesanan == 14:
            input_id = 14
            input_nama_brg = 'Matras'
            input_harga_brg = 3000
        else:
            input_id = 'not found'
            input_nama_brg = 'not found'
            input_harga_brg = 0

        return input_id, input_nama_brg, input_harga_brg

    def input_data_sewaan(id, nama_brg, harga_brg):
        sewaan = {
            'id' : id,
            'nama barang' : nama_brg,
            'harga barang' : harga_brg
        }

        data_sewaan.append(sewaan)


    awal_pilihan = input('Apakah anda ingin menyewa ? y/n : ').upper()
    if awal_pilihan == 'Y' :
        clear_screen()
        print('='*19, 'LIST BARANG OUTDOOR', '='*20)
        print('-'*60)
        print(f"|{'Id':^2} | {'Nama Barang':^35} | {'Harga/hari':^15}|")
        print('-'*60)
        for i in range (len(lb)):
            print(f"|{lb[i]['id']:<2} | {lb[i]['nama barang']:<35} | {lb[i]['harga barang']:<15}|")
        print('-'*60)

        print()

        print('='*60)
        nama = input('Silahkan masukkan nama anda : ')
        no_hp = int(input('Silahkan masukkan no HP anda [0 diganti 62] : '))
        print('='*60)

        print()

        def tampilkan_data():
            print('-'*60)
            for i in range (len(data_sewaan)):
                print(f"* Barang {i+1} \n Id : {data_sewaan[i]['id']} \n Nama barang : {data_sewaan[i]['nama barang']}\n Harga barang : {data_sewaan[i]['harga barang']}")
            print('-'*60)


        print('-'*60)
        kali_jenis = int(input('Berapa banyak jenis barang yang akan anda sewa : '))
        for i in range (kali_jenis):
            print('* Barang', i+1)
            data = pilih_barang_disewa()
            input_data_sewaan(data[0], data[1], data[2])
        print('-'*60)
        clear_screen()

        tampilkan_data()

        cek_data = 'N'
        while cek_data == 'N':
            cek_data = input('Apakah data diatas sudah benar [y/n] : ').upper()
            if cek_data == 'N':
                print('''
                1. Update data
                2. Hapus data
                ''')
                while True :
                    pilihan_cek_data = int(input('Datanya mau dihapus atau di update ? [inputkan angka!] : '))
                    if pilihan_cek_data == 1: #UPDATE DATA SEWAAN
                        clear_screen()
                        tampilkan_data()
                        pilihan_update_data = int(input('Barang ke berapa yang mau di update : '))
                        data = pilih_barang_disewa()
                        data_sewaan[pilihan_update_data-1] = {
                            'id' : data[0],
                            'nama barang' : data[1],
                            'harga barang' : data[2]
                        }
                        clear_screen()
                        tampilkan_data()
                        break
                    elif pilihan_cek_data == 2: #HAPUS DATA SEWAAN
                        pilihan_hapus_data = int(input('Barang ke berapa yang mau di hapus : '))
                        clear_screen()
                        del data_sewaan [pilihan_hapus_data-1]
                        tampilkan_data()
                        break
                    else : print (pilihan_cek_data, 'tidak ada di menu !')

        print('-'*60)
        for i in range(len(data_sewaan)):
            print('* Barang ke', i+1)
            qty = int(input('Masukkan jumlah barang yang disewa : '))
            qty_sewaan.append(qty)
        print('-'*60)

        print('='*19 ,'KETENTUAN WAKTU SEWA', '='*19)
        print('''
        1. Lama waktu sewa tidak boleh kurang dari 1 hari
        2. Sewa lebih dari 3 hari diskon 15%
        3. Sewa lebih dari 5 hari diskon 25%
        ''')
        waktu_sewa = int(input('Berapa hari anda akan menyewa : '))
        while waktu_sewa < 1:
            print('Waktu sewa tidak boleh kurang dari dari 1 hari !')
            waktu_sewa = int(input('Masukkan ulang berapa hari anda akan menyewa : '))
            
        random = random_id()

        def struk():
            print('Id Pesanan :', random)
            print('Nama penyewa :', nama)
            print('No HP : ',no_hp)
            print('-'*60)
            jumlah_harga_barang = []
            for i in range (len(data_sewaan)):                          # MENGALIKAN HARGA SATUAN DENGAN QTY
                hasil = data_sewaan[i]['harga barang'] * qty_sewaan[i]
                jumlah_harga_barang.append(hasil)
            for i in range(len(data_sewaan)):                           # MENAMPILKAN LIST DATA SEWAAN
                print(f"{data_sewaan[i]['nama barang']:<39}{qty_sewaan[i]:<6}{data_sewaan[i]['harga barang']:<5}{jumlah_harga_barang[i]:>10}")
            print(f"{'-'*22:>60}")
            jumlah = 0
            for i in range (len(data_sewaan)):                          # MENJUMLAHKAN DAN MENAMPILKAN HASIL KALI DARI HARGA SATUAN SEWAAN DENGAN QTY
                jumlah = jumlah + jumlah_harga_barang[i]
            print(f"{jumlah:>60}")
            print('-'*60)
            print(f"Waktu sewa (hari) : {waktu_sewa:>40}")
            print('-'*60)
            
            global diskon
            diskon = 0

            if waktu_sewa >= 3 and waktu_sewa < 5:
                diskon = (jumlah * waktu_sewa) * 0.15
            elif waktu_sewa >= 5:
                diskon = (jumlah * waktu_sewa) * 0.25

            global subtotal
            subtotal = jumlah * waktu_sewa

            global total_bayar
            total_bayar = subtotal - diskon

            print(f"Subtotal :{int(subtotal):>50}")
            print(f"Diskon : {int(diskon):>51}")
            print(f"Total Pembayaran : {int(total_bayar):>41}")

        clear_screen()                                              #INVOICE PEMESANAN
        print('-'*60)                                              
        print('='*20 ,'INVOICE PEMESANAN', '='*21)
        print('-'*60)
        struk()

        print('-'*60)
        print()

        tunai = 0
        while tunai < total_bayar:
            tunai = int(input('Masukkan tunai : '))
            if tunai < total_bayar :
                print('Uang anda kurang ulangi !')

        kembalian = tunai - total_bayar

        clear_screen()                                              #STRUK PEMBAYARAN
        print('-'*60)                                           
        print('='*21 ,'STRUK PEMBAYARAN', '='*21)
        print('-'*60)
        struk()
        print(f"Tunai : {tunai:>52}")
        print(f"Kembali : {int(kembalian):>50}")
        print('-'*60)

        TEMPLATE_HISTORY = {
            "id pesanan" : random,
            "nama penyewa" : nama,
            "no hp" : no_hp,
            "barang sewaan" : data_sewaan,
            "waktu sewa" : waktu_sewa,
            "subtotal" : subtotal,
            "diskon" : diskon,
            "total bayar" : total_bayar,
            "tunai" : tunai,
            "kembali" : kembalian
        }

        insert_data(TEMPLATE_HISTORY)

        print(f"\n{'TERIMAKASIH TELAH MEMPERCAYAI DAN MENYEWA BARANG KAMI :)':^60}")
        
    else:
        print()
        print('='*4, 'TERIMAKASIH TELAH MAMPIR WALAUPUN TIDAK MENYEWA :(', '='*4)