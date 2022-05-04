def olah_data(isi_data) :
    data_kehadiran = {}

    for kehadiran in isi_data :
        kehadiran = kehadiran.split()
        data_kehadiran[kehadiran[0]] = kehadiran[1:].count("1")

    return data_kehadiran


def report(data_kehadiran) :
    data_ujian = []

    for kehadiran in data_kehadiran :
        presentase = data_kehadiran[kehadiran] * (1/7 * 100)

        if presentase >= 75 :
            data_ujian.append(kehadiran)

    return data_ujian


def top(data_kehadiran) :
    kehadiran_terkecil = min(data_kehadiran, key=data_kehadiran.get)   

    return kehadiran_terkecil


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    data_kehadiran = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Data Kehadiran" + "\n" +
                  "2. NIM Mahasiswa Yang Boleh Mengikuti Ujian" + "\n" +
                  "3. NIM Yang Paling Malas" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Data Kehadiran")
                print(data_kehadiran, "\n")

            elif input_user == 2 :
                data_ujian = report(data_kehadiran)
                print("\n" + "NIM Yang Diperbolehkan :")

                for ujian in data_ujian :
                    print("-> " + ujian)
                print()

            elif input_user == 3 :
                kehadiran_terkecil = top(data_kehadiran)

                print("\n" + "NIM Siswa Paling Malas Adalah " + kehadiran_terkecil + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")