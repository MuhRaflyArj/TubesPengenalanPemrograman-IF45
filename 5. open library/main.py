def olah_data(isi_data) :
    data_buku = {}

    for buku in isi_data :
        buku = buku.split()
        data_buku[buku[0]] = sum([int(i) for i in buku[2:]])

    return data_buku


def favorit(data_buku) :
    buku_terbanyak = ""
    jumlah_terbanyak = 0

    for buku in data_buku :
        if data_buku[buku] > jumlah_terbanyak :
            buku_terbanyak = buku
            jumlah_terbanyak = data_buku[buku]

    return buku_terbanyak, jumlah_terbanyak


def laporan_stok(isi_data) :
    buku_restock = []

    for buku in isi_data :
        buku = buku.split()

        if int(buku[1]) <= sum([int(i) for i in buku[2:]]) :
            buku_restock.append(buku[0])

    return buku_restock

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    data_buku = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Data Buku" + "\n" +
                  "2. Buku Yang Paling Banyak Dipinjam" + "\n" +
                  "3. Laporan Stok Buku" + "\n" +
                  "4. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Data Buku")
                print(data_buku, "\n")
            
            elif input_user == 2 :
                buku_terbanyak, jumlah_terbanyak = favorit(data_buku)
                print("\n" + f"Buku yang terbanyak dipinjam adalah {buku_terbanyak}" + "\n" +
                      f"sebanyak {jumlah_terbanyak} buku" + "\n")


            elif input_user == 3 :
                buku_restock = laporan_stok(isi_data)
                
                print("\n" + "Buku yang perlu di-restock")
                
                for buku in buku_restock :
                    print(f"-> {buku}")
                print()

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")
        
        except ValueError :
            print("\n" + "Input Salah!!" + "\n")