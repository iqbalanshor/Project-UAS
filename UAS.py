# Dictionary Harga Menu Makanan dan Minuman
from ast import main


menu = {
    '1' : {'item': 'Nasi Liwet',        'harga': 40000},
    '2' : {'item': 'Ikan Gurame Bakar', 'harga': 50000},
    '3' : {'item': 'Ikan Asin',         'harga': 15000},
    '4' : {'item': 'Ayam Goreng',       'harga': 20000},
    '5' : {'item': 'Ayam Bakar',        'harga': 25000},
    '6' : {'item': 'Es teh',            'harga': 10000},
    '7' : {'item': 'Es jeruk',          'harga': 17000},
    '8' : {'item': 'Jus Mangga',        'harga': 20000},
    '9' : {'item': 'Jus Jambu',         'harga': 20000},
    '10': {'item': 'Air Mineral',       'harga': 10000},
}

def tampilkan_menu(daftar):
    print("{:<10} {:<25} {:<15}".format('No', 'Nama', 'Harga'))
    print("---------------------------------------------")
    for nomor, detail in daftar.items():
        print("{:<10} {:<25} Rp {:<15}".format(nomor, detail['item'], detail['harga']))

def pesan_makanan():
    pesanan = {}
    while True:
        tampilkan_menu(menu)
        pilihan = input("Pilih nomor menu (atau ketik '0' untuk mengakhiri): ")
        
        if pilihan.lower() == '0':
            break
        
        if pilihan in menu:
            jumlah = int(input(f"Jumlah {menu[pilihan]['item']}: "))
            pesanan[menu[pilihan]['item']] = {'jumlah': jumlah, 'harga': menu[pilihan]['harga']}
        else:
            print("Pilihan tidak valid. Silakan pilih nomor menu yang benar.")
    return pesanan
    
def hitung_total(pesanan):
    total = 0
    for item, info in pesanan.items():
        total += info['jumlah'] * info['harga']
    return total
    
def cetak_struk(pesanan, total_harga):
    print("\n--- Struk Pembelian ---")
    for item, info in pesanan.items():
        print(f"{info['jumlah']} {item} - Rp {info['jumlah'] * info['harga']}")
    print("----------------------")
    print(f"Total Harga: Rp {total_harga}")
    print("Terima kasih atas pembelian Anda!")

print("=================================")
print("           KANTIN ANSHOR         ")
print("=================================")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli)

daftar_pesanan = pesan_makanan()
total_harga = hitung_total(daftar_pesanan)
cetak_struk(daftar_pesanan, total_harga)

if __name__ == "__main__":
    main()