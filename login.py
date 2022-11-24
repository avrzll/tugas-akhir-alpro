import os
import crud
from main import proses_sewa

barang_sewaan_new = []

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

    data_sewaan_new.append(sewaan)

def clear_screen():
    sistem_operasi = os.name

    if sistem_operasi == 'posix':
        os.system('clear')
    elif sistem_operasi == 'nt' :
        os.system('cls')


def input_data_sewaan(id, nama_brg, harga_brg):
    sewaan = {
        'id' : id,
        'nama barang' : nama_brg,
        'harga barang' : harga_brg
    }

    barang_sewaan_new.append(sewaan)


print('\n\n')
print('-'*60)
print('='*5, 'SELAMAT DATANG DI PROGRAM PENYEWAAN ALAT OUTDOOR', '='*5)
print('-'*60)


print('''
1. Login sebagai admin
2. Login sebagai penyewa
''')
login = int(input('Login sebagai admin atau penyewa : '))
if login == 1 :
    clear_screen()
    user = input('Masukkan username : ')
    pw = int(input('Masukkan password : '))
    if user == 'admin' and pw == 0000:
        while True:
            clear_screen()
            print('-'*60)
            print('='*11 ,'HALAMAN ADMIN PENYEWAAN ALAT OUTDOOR', '='*11)
            print('-'*60)
            print(f"{'='*11}{' '*10}{'1. Tampilkan data'}{' '*12}{'='*10}")
            print(f"{'='*11}{' '*10}{'2. Update data'}{' '*15}{'='*10}")
            print(f"{'='*11}{' '*10}{'3. Hapus data'}{' '*16}{'='*10}")
            print(f"{'='*11}{' '*10}{'4. Keluar program'}{' '*12}{'='*10}")
            print('-'*60)
            print()
            menu = int(input('Pilih menu : '))
            if menu == 1:
                crud.view_data()
                print()
                input('Press enter to continue...')
            elif menu == 2:
                id_pesanan = input('Masuukan id pesanan yang akan di update : ')    
                nama_penyewa_new = input('Nama Penyewa : ')
                no_hp_new = int(input('No HP : '))
                kali_jenis = int(input('Berapa banyak barang jenis barang yang akan di update : '))
                for i in range(kali_jenis):
                    print('* Barang', i+1)
                    data = pilih_barang_disewa()
                    input_data_sewaan(data[0], data[1], data[2])
                waktu_sewa_new = int(input('Waktu sewa : '))
                subtotal_new = int(input('Subtotal : '))
                diskon_new = int(input('Diskon : '))
                total_bayar_new = int(input('Total Bayar : '))
                tunai_new = int(input('Tunai : '))
                kembali_new = int(input('Kembali : '))

                crud.update_data(id_pesanan, nama_penyewa_new, no_hp_new, barang_sewaan_new, waktu_sewa_new, subtotal_new, diskon_new, total_bayar_new, tunai_new, kembali_new)
                print()
                input('Press enter to continue...')
            elif menu == 3:
                crud.view_data()
                input_id = input('Masukkan id pesanan yang akan dihapus : ')
                crud.delete_data(input_id)
                print()
                input('Press enter to continue...')
            elif menu == 4:
                break
        print('Anda keluar program...')
            

    else : 
        print()
        print('Username / password anda salah !')
        print('Anda keluar program...')


elif login == 2 :
    clear_screen()
    proses_sewa()