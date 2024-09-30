while True :
    harga = int(input("Masukkan harga barang : "))
    jumlah = int(input("Masukkan jumlah barang : "))

    bayar = harga * jumlah

    if bayar > 250000 :
        diskon = bayar * 25/100
        total = bayar - diskon
        print("=== Anda mendapatkan diskon 25% ===")
    elif bayar < 250000 :
        total = bayar
        print("=== Anda tidak mendapatkan diskon ===    ")
    else : 
        print("Anda tidak mendapatkan diskon")

    print("Total harga yang harus dibayar : ",total)

    lanjut = input("Apakah anda ingin menghitung total harga lagi? (y/n) : ")
    if lanjut.lower() != 'y' :
        break

print("Terimakasih!!!!")