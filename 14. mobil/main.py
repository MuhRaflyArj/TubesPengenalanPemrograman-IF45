def olah_data(isi_data) :
    daftar_mobil = {}

    for mobil in isi_data :
        mobil = mobil.split("#")
        data_mobil = [mobil[1], mobil[2], int(mobil[3])]

        daftar_mobil[mobil[0]] = data_mobil

    return daftar_mobil

def report(daftar_mobil) :
    terbanyak = max([daftar_mobil[mobil][2] for mobil in daftar_mobil])
    tersedikit = min([daftar_mobil[mobil][2] for mobil in daftar_mobil])

    nama_terbanyak = [mobil for mobil in daftar_mobil if daftar_mobil[mobil][2] == terbanyak][0]
    nama_tersedikit = [mobil for mobil in daftar_mobil if daftar_mobil[mobil][2] == tersedikit][0]

    return nama_terbanyak, nama_tersedikit

def bahan_bakar(daftar_mobil, nama_mobil) :
    return [daftar_mobil[mobil][1] for mobil in daftar_mobil if mobil == nama_mobil]



if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    daftar_mobil = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Daftar Mobil" + "\n" +
                  "2. Stok Mobil Terbanyak dan Tersedikit" + "\n" +
                  "3. Cari Bahan Bakar Mobil" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Daftar Mobil")
                print(daftar_mobil, "\n")

            elif input_user == 2 :
                terbanyak, tersedikit = report(daftar_mobil)

                print("\n" + "Stok Mobil Terbanyak Adalah : " + terbanyak)
                print("Stok Mobil Tersedikit Adalah : " + tersedikit + "\n")

            elif input_user == 3 :
                list_mobil = [mobil for mobil in daftar_mobil]
                print("\n" + "Daftar Mobil")

                for i in range(len(list_mobil)) :
                        print(str(i+1) + ". " + list_mobil[i])
                
                input_mobil = int(input("Masukkan Menu : "))

                if input_mobil > 0 and input_mobil < len(list_mobil) + 1 :
                    jenis_bensin = bahan_bakar(daftar_mobil, list_mobil[input_mobil-1])
                    print("\n" + list_mobil[input_mobil-1] + " Menggunakan Bahan Bakar " + jenis_bensin[0] + "\n")

                else :
                    print("\n" + "Input Tidak ada di Menu" + "\n")


            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else : 
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")