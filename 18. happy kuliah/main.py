def olah_data(isi_data) :
    rekap_kehadiran = [kehadiran.split() for kehadiran in isi_data]
    data_kehadiran = {}

    minggu = 1
    for i in range(1, 8) :
        data_kehadiran[f"minggu-{minggu}"] = len([rekap_kehadiran[j][i] for j in range(len(rekap_kehadiran)) if rekap_kehadiran[j][i] == "1"])
        minggu += 1
        
    return data_kehadiran


def report(data_kehadiran) :
    rekap_kehadiran = [data_kehadiran[f"minggu-{i}"] for i in range(1,8)]

    naik, turun = True, True
    for i in range(1, len(rekap_kehadiran)) :
        if rekap_kehadiran[i] > rekap_kehadiran[i-1] :
            turun = False
        elif rekap_kehadiran[i] < rekap_kehadiran[i-1] :
            naik = False


    if sum(rekap_kehadiran) // len(rekap_kehadiran) == rekap_kehadiran[0] :
        return "tetap"
    elif naik :
        return "naik"
    elif turun :
        return "turun"
    else :
        return "tidak berpola"


def rerata(data_kehadiran) :
    return round(sum([data_kehadiran[f"minggu-{i}"] for i in range(1,8)]) / len(data_kehadiran), 2)


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    data_kehadiran = olah_data(isi_data)
    
    while True :
        try :
            print("1. Dictionary Data Kehadiran" + "\n" +
                  "2. Tren Kehadiran" + "\n" +
                  "3. Rata-Rata Kehadiran" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Data Kehadiran")
                print(data_kehadiran, "\n")

            elif input_user == 2 :
                tren = report(data_kehadiran)
                print("\n" + "Tren Kehadiran Adalah " + tren + "\n")

            elif input_user == 3 :
                rerata_kehadiran = rerata(data_kehadiran)
                print("\n" + "Rata-Rata Kehadiran Perminggu Adalah " + str(rerata_kehadiran) + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")
