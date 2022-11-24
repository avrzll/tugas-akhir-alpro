import json
filename = 'data_sewaan.json'

def insert_data(TEMPLATE_HISTORY):
    with open(filename, 'r') as jsonFile:
        data = json.load(jsonFile)
        histori = data['histori sewaan']
        histori.append(TEMPLATE_HISTORY)
    with open(filename, 'w') as jsonFile:
        json.dump(data, jsonFile, indent=3)

def view_data():
    with open(filename, 'r') as jsonFile:
        data = json.load(jsonFile)
        histori = data['histori sewaan']
        num = 1
        for i in histori :
            id_pesanan = i['id pesanan']
            nama_penyewa = i['nama penyewa']
            no_hp = i['no hp']
            barang_sewaan = i['barang sewaan']
            waktu_sewa = i['waktu sewa']
            subtotal = i['subtotal']
            diskon = i['diskon']
            total_bayar = i['total bayar']
            tunai = i['tunai']
            kembali = i['kembali']

            print('\n\n')
            print('* Data ke :', num)
            print()
            print('Id pesanan :', id_pesanan)
            print('Nama penyewa :', nama_penyewa)
            print('No hp :', no_hp) 
            print('Barang sewaan :', barang_sewaan)
            print('Waktu sewa :', waktu_sewa)
            print('Subtotal :', subtotal)
            print('Diskon :', diskon)
            print('Total bayar :', total_bayar)
            print('Tunai :', tunai)
            print('Kembali :', kembali)

            num += 1

def delete_data(input_id):
    with open(filename, 'r') as jsonFile:
        data = json.load(jsonFile)
        histori = data['histori sewaan']
        for i in range(len(histori)):
            if histori[i]['id pesanan'] == input_id:
                del histori[i]
                break

    with open(filename, 'w') as jsonFile:
        json.dump(data, jsonFile, indent=3)


def update_data(id_pesanan, nama_penyewa_new, no_hp_new, barang_sewaan_new, waktu_sewa_new, subtotal_new, diskon_new, total_bayar_new, tunai_new, kembali_new):
    with open(filename, 'r') as jsonFile:
        data = json.load(jsonFile)
        histori = data['histori sewaan']
        for i in histori:
            if i ['id pesanan'] == id_pesanan:
                i['nama penyewa'] = nama_penyewa_new
                i['no hp'] = no_hp_new
                i['barang sewaan'] =  barang_sewaan_new
                i['waktu sewa'] = waktu_sewa_new
                i['subtotal'] = subtotal_new
                i['diskon'] = diskon_new
                i['total bayar'] = total_bayar_new
                i['tunai'] = tunai_new
                i['kembali'] = kembali_new

    with open(filename, 'w') as jsonFile:
        json.dump(data, jsonFile, indent=3)