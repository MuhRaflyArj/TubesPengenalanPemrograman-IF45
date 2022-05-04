def olah_data(isi_data) :
    klasemen = []

    for pertandingan in isi_data :
        data_pertandingan = {}
        pertandingan = pertandingan.split()

        data_pertandingan["nama"] = pertandingan[0]
        data_pertandingan["poin"] = int(pertandingan[1]) * 3 + int(pertandingan[2])
        data_pertandingan["selisih gol"] = int(pertandingan[4]) - int(pertandingan[5])

        klasemen.append(data_pertandingan)

    return klasemen


def juara_liga(klasemen) :
    tim_juara = ""
    skor_tertinggi = 0

    for pertandingan in klasemen :
        if pertandingan["poin"] > skor_tertinggi :
            skor_tertinggi = pertandingan["poin"]
            tim_juara = pertandingan["nama"]

    return tim_juara


def cari(klasemen, skor) :
    nama_tim = []

    for pertandingan in klasemen :
        if pertandingan["poin"] < skor :
            nama_tim.append(pertandingan["nama"])

    return nama_tim


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()
    
    klasemen = olah_data(isi_data)

    while True :
        try :
            print("1. List Klasemen" + "\n" +
                  "2. Juara Liga" + "\n" +
                  "3. Cari Tim" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Klasemen")
                print(klasemen, "\n")

            elif input_user == 2 :
                juara = juara_liga(klasemen)
                
                print("\n" + "Juara liga adalah " + juara + "\n")

            elif input_user == 3 :
                input_poin = int(input("\nMasukkan Skor : "))

                list_tim = cari(klasemen, input_poin)

                if len(list_tim) > 0 :
                    print("\n" + "Tim Dengan Nilai Poin Kurang Dari " + str(input_poin) + " : ")

                    for tim in list_tim :
                        print("-> " + tim)
                    print()

                else :
                    print("\n" + "Tidak Ada Tim Dengan Skor Kurang Dari " + str(input_poin) + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")
        except ValueError :
            print("\n" + "Input Salah!!" + "\n")