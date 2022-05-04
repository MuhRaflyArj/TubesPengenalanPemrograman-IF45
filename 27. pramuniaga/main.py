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

def penghasilan(penjualan) :
    hasil_penjualan = [{"nama" : data["nama"], "penjualan" : sum(list(data.values())[1:])} for data in penjualan]

    return hasil_penjualan

def bonus(penjualan) :
    hasil_penjualan = penghasilan(penjualan)
    penghasilan_pramuniaga = []

    for data in hasil_penjualan :
        data_pramuniaga = {}

        if data["penjualan"] > 20000 :
            data_pramuniaga["nama"] = data["nama"]
            data_pramuniaga["penghasilan"] = 500 + round(data["penjualan"] * 0.025, 2) + 1000

            penghasilan_pramuniaga.append(data_pramuniaga)

    return penghasilan_pramuniaga


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    penjualan = olah_data(isi_data)

    while True :
        try :
            print("1. List Penjualan" + "\n" +
                  "2. Penghasilan Pramuiaga" + "\n" +
                  "3. Hasil Bonus Pramuniaga" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Penjualan")
                print(penjualan, "\n")

            elif input_user == 2 :
                hasil_penjualan = penghasilan(penjualan)
                print("\n" + "Data Penghasilan Penjualan")

                for data in hasil_penjualan :
                    nama_penjualan, total_penjualan = data["nama"], data["penjualan"]
                    print("\t" + f"Hasil Penjualan {nama_penjualan} Selama Seminggu Sebesar {total_penjualan}")
                print()

            elif input_user == 3 :
                penghasilan_pramuniaga = bonus(penjualan)
                print("\n" + "Data Bonus Pramuniaga")

                for data in penghasilan_pramuniaga :
                    nama_bonus, total_penghasilan = data["nama"], data["penghasilan"]
                    print("\t" + f"{nama_bonus} Mendapat Bonus dan Memiliki Penghasilan Total Sebesar {total_penghasilan}")
                print()

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")