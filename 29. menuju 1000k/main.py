def olah_data(isi_data) :
    catatan_lari = [i.split() for i in isi_data]
    catatan = {}

    for data in catatan_lari :
        if data[0].split("/")[1] not in list(catatan.keys()) :
            catatan[data[0].split("/")[1]] = int(data[1])
        elif data[0].split("/") in list(catatan.keys()) :
            catatan[data[0].split("/")[1]] += int(data[1])

    return catatan

def rekor(catatan) :
    return [data for data in catatan if catatan[data] == max(list(catatan.values()))]

def report(catatan) :
    return round(sum(list(catatan.values())) / len(list(catatan.values())), 2)


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    catatan = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Catatan" + "\n" +
                  "2. Jarak Terjauh" + "\n" +
                  "3. Rata-Rata Setiap Bulan" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Catatan")
                print(catatan, "\n")

            elif input_user == 2 :
                jarak_terjauh = rekor(catatan)
                print("\n" + "Jarak Terjauh Ditempuh Pada Bulan " + ", ".join(jarak_terjauh) + "\n")

            elif input_user == 3 :
                rerata_jarak = report(catatan)
                print("\n" + f"Rata-Rata Jarak Lari Sebesar {rerata_jarak}km" + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")