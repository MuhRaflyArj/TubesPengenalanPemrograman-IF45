def olah_data(isi_data) :
    data_penjualan = [i.split() for i in isi_data]
    penjualan = []

    for data in data_penjualan :
        hasil_penjualan = {}

        hasil_penjualan["nama"] = data[0]
        hasil_penjualan["senin"] = int(data[1])
        hasil_penjualan["selasa"] = int(data[2])
        hasil_penjualan["rabu"] = int(data[3])
        hasil_penjualan["kamis"] = int(data[4])
        hasil_penjualan["jumat"] = int(data[5])

        penjualan.append(hasil_penjualan)

    return penjualan

def tertinggi(penjualan) :
    total_penjualan = max([sum(list(i.values())[1:]) for i in penjualan])
    penjualan_terbanyak = []

    for data in penjualan :
        if sum(list(data.values())[1:]) == total_penjualan :
            penjualan_terbanyak.append(data["nama"])

    return penjualan_terbanyak

def report(penjualan) :
    total_penjualan = [list(i.values())[1:] for i in penjualan]
    daftar_hari = ["senin", "selasa", "rabu", "kamis", "jumat"]
    rerata_penjualan = {}

    for i in range(len(total_penjualan[0])) :
        total = 0

        for j in range(len(total_penjualan)) :
            total += total_penjualan[j][i]

        rerata_penjualan[daftar_hari[i]] = round(total/len(total_penjualan[0]), 2)

    return rerata_penjualan

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    penjualan = olah_data(isi_data)

    while True :
        try :
            print("1. List Penjualan" + "\n" +
                  "2. Penjualan Tertinggi" + "\n" +
                  "3. Rata-Rata Penjualan" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Penjualan")
                print(penjualan, "\n")

            elif input_user == 2 :
                penjualan_terbanyak = tertinggi(penjualan)
                print("\n" + "Penjual dengan penjualan tertinggi adalah " + ", ".join(penjualan_terbanyak) + "\n")

            elif input_user == 3 :
                rerata_penjualan = report(penjualan)
                print("\n" + "Data Rerata Penjualan Selama Seminggu")

                for rerata in rerata_penjualan :
                    print("\t" + f"Rerata Penjualan Pada Hari {rerata} adalah {rerata_penjualan[rerata]}")
                print()
                
            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")