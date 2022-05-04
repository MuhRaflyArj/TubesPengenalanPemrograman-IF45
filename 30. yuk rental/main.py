def olah_data(isi_data) :
    data_rental = [i.split() for i in isi_data]
    rental = {}

    for data in data_rental :
        data_sewa = {}

        if data[1] not in rental :
            data_sewa["bulan"] = [int(data[0].split("-")[1])]
            data_sewa["total"] = [int(data[2])]

            rental[data[1]] = data_sewa
        
        elif data[1] in rental :
            rental[data[1]]["bulan"].append(int(data[0].split("-")[1]))
            rental[data[1]]["total"].append(int(data[2]))

    return rental

def favorit(rental) :
    return [data.capitalize() for data in rental if sum(rental[data]["total"]) == max([sum(rental[i]["total"]) for i in rental])]

def report(rental, mobil) :
    bulan, total = rental[mobil]["bulan"], rental[mobil]["total"]
    data_rerata = {"bulan" : [], "rerata" : []}

    for i in list(set(bulan)) :
        data_rerata["bulan"].append(i)
        jumlah_penyewa, banyak_bulan = 0, bulan.count(i)

        for j in range(bulan.count(i)) :
            indeks = bulan.index(i)
            jumlah_penyewa += total[indeks]

            bulan.pop(indeks); total.pop(indeks)

        data_rerata["rerata"].append(round(jumlah_penyewa/banyak_bulan, 2))

    return data_rerata

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    rental = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Rental" + "\n" +
                  "2. Mobil Paling Banyak Disewa" + "\n" +
                  "3. Rata-Rata Sewa Mobil" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Rental")
                print(rental, "\n")

            elif input_user == 2 :
                sewa_terbanyak = favorit(rental)
                print("\n" + "Mobil Yang Disewa Terbanyak Pada 2021 Adalah " + ", ".join(sewa_terbanyak) + "\n")

            elif input_user == 3 :
                input_mobil = input("\n" + "Nama Mobil Yang Akan Dicari : ").lower()

                if input_mobil in list(rental.keys()) :
                    data_rerata = report(rental, input_mobil)

                    print("\n" + f"Rata-Rata Sewa Mobil {input_mobil.capitalize()}")

                    for i in range(len(data_rerata["rerata"])) :
                        bulan, rerata = data_rerata["bulan"][i], data_rerata["rerata"][i]
                        print("\t" + f"Rata-Rata Sewa Bulan {bulan} sebsesar {rerata}")
                    print()

                else :
                    print("\n" + "Nama Mobil Tidak Terdaftar" + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")