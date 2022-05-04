def olah_data(isi_data) :
    data_tabungan = [i.split() for i in isi_data]
    pemasukan, pengeluaran = {}, {}

    for data in data_tabungan :
        if data[2][0] == "+" :
            if data[0] not in list(pemasukan.keys()) :
                pemasukan[f"{data[0]} {data[1]}"] = int(data[2][1:])
            else :
                pemasukan[data[0]] += int(data[2][1:])

        elif data[2][0] == "-" :
            if data[0] not in list(pengeluaran.keys()) :
                pengeluaran[f"{data[0]} {data[1]}"] = int(data[2][1:])

    return pemasukan, pengeluaran

def rerata(pemasukan, pengeluaran) :
    rerata_pemasukan, rerata_pengeluaran = {}, {}

    for data in pemasukan :
        if data.split()[0] not in rerata_pemasukan :
            rerata_pemasukan[data.split()[0]] = [pemasukan[data]]
        else :
            rerata_pemasukan[data.split()[0]].append(pemasukan[data])

    for data in pengeluaran :
        if data.split()[0] not in rerata_pengeluaran :
            rerata_pengeluaran[data.split()[0]] = [pengeluaran[data]]
        else :
            rerata_pengeluaran[data.split()[0]].append(pengeluaran[data])

    for data in rerata_pemasukan :
        rerata_pemasukan[data] = round(sum(rerata_pemasukan[data]) / len(rerata_pemasukan[data]), 2)
    for data in rerata_pengeluaran :
        rerata_pengeluaran[data] = round(sum(rerata_pengeluaran[data]) / len(rerata_pengeluaran[data]), 2)

    return rerata_pemasukan, rerata_pengeluaran

def report(pemasukan) :
    return [data for data in pemasukan if pemasukan[data] == max(list(pemasukan.values()))]


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()[:-1]
    data.close()

    pemasukan, pengeluaran = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Pemasukkan dan Pengeluaran" + "\n" +
                  "2. Rerata Pemasukkan" + "\n" +
                  "3. Pemasukkan Tertinggi" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Pemasukan")
                print(pemasukan)

                print("\n" + "Dictionary pengeluaran")
                print(pengeluaran, "\n")

            elif input_user == 2 :
                rerata_pemasukan, rerata_pengeluaran = rerata(pemasukan, pengeluaran)
                
                print("\n" + "Rata-Rata Pengeluaran Setiap Bulan")
                for data in rerata_pemasukan :
                    print("\t" + f"Rerata Pemasukan Bulan {data} Sebesar {rerata_pemasukan[data]}")

                print("\n" + "Rata-Rata Pengeluaran Setiap Bulan")
                for data in rerata_pengeluaran :
                    print("\t" + f"Rerata Pemasukkan Bulan {data} Sebesar {rerata_pengeluaran[data]}")
                print()

            elif input_user == 3 :
                pemasukan_tertinggi = report(pemasukan)
                print("\n" + f"Pemasukan Tertinggi Terjadi Pada Bulan " + ", ".join(pemasukan_tertinggi) + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")