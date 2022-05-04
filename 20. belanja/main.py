def olah_data(isi_data) :
    data_toko = [i.split() for i in isi_data]
    toko = {}

    for i in range(1, len(data_toko[0])) :
        data_barang = {}
        for j in range(len(data_toko)) :
            data_barang[data_toko[j][0]] = int(data_toko[j][i].replace(".", ""))
        toko[f"toko {i}"] = data_barang
    
    return toko

def termurah(toko) :
    daftar_barang = list(toko["toko 1"].keys())
    daftar_termurah = {}

    for barang in daftar_barang :
        harga_termurah = min([toko[nama_toko][barang] for nama_toko in toko])
        daftar_termurah[barang] = [nama_toko for nama_toko in toko if toko[nama_toko][barang] == harga_termurah]
    
    return daftar_termurah

def report(toko) :
    daftar_barang = list(toko["toko 1"].keys())
    daftar_rerata = {}

    for barang in daftar_barang :
        daftar_harga = [toko[nama_toko][barang] for nama_toko in toko]
        daftar_rerata[barang] = round(sum(daftar_harga) / len(daftar_harga), 2)

    return daftar_rerata
            


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    toko = olah_data(isi_data)
    report(toko)

    while True :
        try :
            print("1. Dictionary Toko" + "\n" +
                  "2. Barang Termurah" + "\n" +
                  "3. Rata-rata Harga Barang" + "\n" +
                  "4. Keluar dari Program")
            
            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Toko")
                print(toko, "\n")

            elif input_user == 2 :
                daftar_termurah = termurah(toko)
                nama_barang = list(daftar_termurah.keys())
                
                print("\n" + "Barang Termurah")

                for i in range(len(nama_barang)) :
                    print(f"{i+1}. {nama_barang[i]}")

                input_barang = int(input("Masukkan Nomor Barang : "))

                if input_barang < 1 or input_barang > len(nama_barang) :
                    print("\n" + "Input Tidak ada di Menu" "\n")
                
                else :
                    print("\n" + f"{nama_barang[input_barang-1]} yang termurah terdapat di toko")
                    for nama_toko in daftar_termurah[nama_barang[input_barang-1]] :
                        print("->", nama_toko)
                    print()

            elif input_user == 3 :
                harga_rerata = report(toko)
                print("\n" + "Rata-rata harga barang")

                for nama_barang in harga_rerata :
                    print(f"{nama_barang} : {harga_rerata[nama_barang]}")
                print()


            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")