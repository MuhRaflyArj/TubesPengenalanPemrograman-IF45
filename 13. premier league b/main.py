def olah_data(isi_data) :
    klub = {}

    for pertandingan in isi_data :
        pertandingan = pertandingan.split()

        if pertandingan[0] not in klub :
            klub[pertandingan[0]] = [0, 0]
        if pertandingan[3] not in klub :
            klub[pertandingan[3]] = [0, 0]

        klub[pertandingan[0]][0] += int(pertandingan[1])
        klub[pertandingan[0]][1] += 1

        klub[pertandingan[3]][0] += int(pertandingan[2])
        klub[pertandingan[3]][1] += 1

    return klub


def dashboard(klub) :
    data_klub = {}

    for pertandingan in klub :
        data_klub[pertandingan] = klub[pertandingan][0] / klub[pertandingan][1]

    return data_klub


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    klub = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Klub" + "\n" +
                  "2. Dashboard Pertandingan" + "\n" +
                  "3. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Klub")
                print(klub, "\n")

            elif input_user == 2 :
                data_klub = dashboard(klub)
                print("\n" + "%-16s %-s" % ("Klub", "Rata-Rata Gol"))

                for pertandingan in data_klub :
                    print("%-16s %-s" % (pertandingan, data_klub[pertandingan]))
                print()
                
            elif input_user == 3 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")