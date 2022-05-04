def olah_data(isi_data) :
    list_mobil = []

    for mobil in isi_data :
        mobil = mobil.split("#")
        data_mobil = {}
        
        data_mobil["tipe"] = mobil[0]
        data_mobil["warna"] = mobil[1]
        data_mobil["bahan bakar"] = mobil[2]
        data_mobil["stok"] = int(mobil[3])

        list_mobil.append(data_mobil)

    return list_mobil

def stok_mobil(list_mobil) :
    return sum(mobil["stok"] for mobil in list_mobil)

def tampil_warna(list_mobil) :
    return list(set([mobil["warna"] for mobil in list_mobil]))

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    list_mobil = olah_data(isi_data)

    while True :
        try :
            print("1. Print List Mobil" + "\n" +
                  "2. Jumlah Mobil yang Ada di Dealer" + "\n" +
                  "3. Warna yang Terdapat di Dealer" + "\n" +
                  "4. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Mobil")
                print(list_mobil, "\n")
            
            elif input_user == 2 :
                stok = stok_mobil(list_mobil)
                print("\n" + f"Terdapat {stok} Stok Mobil di Dealer" + "\n")

            elif input_user == 3 :
                warna = tampil_warna(list_mobil)
                print("\n" + f"Warna yang tersedia adalah {', '.join(warna)}" + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")