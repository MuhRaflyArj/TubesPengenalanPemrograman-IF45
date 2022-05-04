def olah_data(isi_data) :
    daftar_penduduk = []

    for penduduk in isi_data :
        penduduk = penduduk.split("#")
        data_penduduk = {}

        data_penduduk["nik"] = int(penduduk[0])
        data_penduduk["nama"] = penduduk[1]
        data_penduduk["tempat"] = penduduk[2]
        data_penduduk["tanggal lahir"] = penduduk[3].replace(" \n", "")

        daftar_penduduk.append(data_penduduk)

    return daftar_penduduk        


def print_penduduk(daftar_penduduk) :
    daftar_usia = []

    for penduduk in daftar_penduduk :
        data_penduduk = {}

        data_penduduk["nama"] = penduduk["nama"]
        data_penduduk["usia"] = 2022 - int(penduduk["tanggal lahir"].split()[2])

        daftar_usia.append(data_penduduk)

    return daftar_usia


def hitung_lahir(daftar_penduduk) :
    daftar_lahir = {}

    for penduduk in daftar_penduduk :
        bulan = penduduk["tanggal lahir"].split()[1]
        if bulan not in daftar_lahir :
            daftar_lahir[bulan] = 1
        else :
            daftar_lahir[bulan] += 1

    return daftar_lahir

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    daftar_penduduk = olah_data(isi_data)

    while True :
        try :
            print("1. Print Daftar Penduduk" + "\n" +
                  "2. Data Usia Penduduk" + "\n" +
                  "3. Data Tempat Lahir" + "\n" +
                  "4. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Daftar Penduduk")
                print(daftar_penduduk, "\n")

            elif input_user == 2 :
                daftar_usia = print_penduduk(daftar_penduduk)
                print("\n" + "Daftar Usia Penduduk")

                for penduduk in daftar_usia :
                    print(f"{penduduk['nama']} Berusia {penduduk['usia']} Tahun")
                print()


            elif input_user == 3 :
                daftar_lahir = hitung_lahir(daftar_penduduk)
                print("\n" + "Jumlah Lahir per Kota")
                
                for penduduk in daftar_lahir :
                    print(f"Sebanyak {daftar_lahir[penduduk]} Orang Lahir di {penduduk}")
                print()



            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")
        
        except ValueError :
            print("\n" + "Input Salah!!" + "\n")