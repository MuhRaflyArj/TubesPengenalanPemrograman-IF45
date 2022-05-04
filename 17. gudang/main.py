def olah_data(isi_data) :
    data_barang = []

    for barang in isi_data :
        barang = barang.split()
        dict_barang = {}

        dict_barang["nama"] = barang[0]

        for i in range(1, len(barang)) :
            if i % 2 != 0 :
                dict_barang[f"produksi minggu-{(i+1)//2}"] = int(barang[i])
            
            elif i % 2 == 0 :
                dict_barang[f"penjualan minggu-{(i+1)//2}"] = int(barang[i])
        
        data_barang.append(dict_barang)

    return data_barang


def peningkatan(data_barang) :
    data_peningkatan = {}

    for barang in data_barang :
        data_peningkatan[barang["nama"]] = True

        for i in range(2,5) :
            if barang[f"produksi minggu-{i-1}"] > barang[f"produksi minggu-{i}"] :
                data_peningkatan[barang["nama"]] = False

    return data_peningkatan


def report(data_barang) :
    data_penjualan = {}

    for barang in data_barang :
        rerata = sum([barang[f"penjualan minggu-{i}"] for i in range(1, 5)]) / 4
        data_penjualan[barang["nama"]] = rerata

    return data_penjualan



if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    data_barang = olah_data(isi_data)

    while True :
        try :
            print("1. List Data Barang" + "\n" +
                  "2. Peningkatan Produksi" + "\n" +
                  "3. Rata-Rata Penjualan" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Data Barang")
                print(data_barang, "\n")

            elif input_user == 2 :
                data_peningkatan = peningkatan(data_barang)

                print("\n" + "Barang Yang Mengalami Peningkatan : ")
                for barang in data_peningkatan :
                    if data_peningkatan[barang] :
                        print("-> " + barang)
                print()

            elif input_user == 3 :
                data_penjualan = report(data_barang)

                print("\n" + "Rata-rata Penjualan : ")
                for barang in data_penjualan :
                    print("Rata-Rata Penjualan " + barang + " adalah " + str(data_penjualan[barang]))
                print()
            
            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")