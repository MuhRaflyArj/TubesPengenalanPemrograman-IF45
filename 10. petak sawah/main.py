def olah_data(isi_data) :
    petak_sawah = []

    for sawah in isi_data :
        data_sawah = {}
        sawah = sawah.split()

        data_sawah["lokasi"] = sawah[0]
        data_sawah["hari"] = int(sawah[1])
        data_sawah["gabah"] = float(sawah[2])
        data_sawah["penjualan"] = int(sawah[3])

        petak_sawah.append(data_sawah)

    return petak_sawah


def report(petak_sawah) :
    total_penjualan = 0
    total_gabah = 0

    for sawah in petak_sawah :
        total_gabah += sawah["gabah"]
        total_penjualan += sawah["gabah"]*1000 * sawah["penjualan"]

    return int(total_penjualan), total_gabah


def rerata(petak_sawah, lokasi) :
    total = 0
    banyak_petak = 0

    for sawah in petak_sawah :
        if sawah["lokasi"] == lokasi.capitalize() :
            total += sawah["gabah"]
            banyak_petak += 1

    if banyak_petak > 0 :
        return total // banyak_petak
    else :
        return 0


def produktif(petak_sawah) :
    nama_terbanyak = ""
    jumlah_terbanyak = 0

    for sawah in petak_sawah :
        if sawah["gabah"] > jumlah_terbanyak :
            nama_terbanyak = sawah["lokasi"]
            jumlah_terbanyak = sawah["gabah"]


    return nama_terbanyak

    
if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    petak_sawah = olah_data(isi_data)


    while True :
        try :
            print("1. List Petak Sawah" + "\n" +
                  "2. Total Gabah dan Penjualan selama Setahun" + "\n" +
                  "3. Rata-Rata Hasil Panen" + "\n" +
                  "4. Sawah Ter-produktif" + "\n" +
                  "5. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Petak Sawah")
                print(petak_sawah, "\n")

            elif input_user == 2 :
                total_penjualan, total_gabah = report(petak_sawah)

                print("\n" + "Total Gabah Per-tahun : " + str(total_gabah))
                print("Total Penjualan Per-tahun : Rp." + str(total_penjualan) + "\n")

            elif input_user == 3 :
                input_rerata = input("\nLokasi Petak : ")
                hasil_rerata = rerata(petak_sawah, input_rerata)

                if hasil_rerata > 0 :
                    print("\n" + "Rata-rata hasil panen di " + input_rerata.capitalize() +
                          " Sebesar " + str(hasil_rerata) + " ton" + "\n")

                else :
                    print("\n" + "Tidak ada petak yang berlokasi di " + input_rerata.capitalize() + "\n")

            elif input_user == 4 :
                terproduktif = produktif(petak_sawah)

                print("\n" + "Petak Sawah Terproduktif Berlokasi di " + terproduktif + "\n")

            elif input_user == 5 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")
