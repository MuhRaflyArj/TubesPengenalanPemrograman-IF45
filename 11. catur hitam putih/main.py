from re import L


def olah_data(isi_data) :
    pertandingan = []

    for catur in isi_data :
        rekap = {}
        catur = catur.split()

        rekap["pemain putih"] = catur[0]
        rekap["pemain hitam"] = catur[1]

        skor = catur[2].split("-")

        if skor[0] == "1/2" :
            skor[0] = 0.5
        if skor[1] == "1/2" :
            skor[1] = 0.5

        rekap["skor putih"] = float(skor[0])
        rekap["skor hitam"] = float(skor[1])

        pertandingan.append(rekap)

    return pertandingan


def report(pertandingan) :
    pertandingan_seri = []

    for catur in pertandingan :
        if catur["skor putih"] == 0.5 :
            pertandingan_seri.append(catur)

    return pertandingan_seri


def poin(pertandingan, pemain) :
    total = 0
    cek = False

    for catur in pertandingan :
        if catur["pemain putih"] == pemain :
            total += catur["skor putih"]
            cek = True

        elif catur["pemain hitam"] == pemain :
            total += catur["skor hitam"]
            cek = True

    return total, cek

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    pertandingan = olah_data(isi_data)

    while True :
        try :
            print("1. List Pertandingan" + "\n" +
                  "2. Pertandingan Berhasil Seri" + "\n" +
                  "3. Poin Pemain" + "\n" +
                  "4. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Pertandingan")
                print(pertandingan, "\n")

            elif input_user == 2 :
                pertandingan_seri = report(pertandingan)

                print("\n" + "Pertandingan Yang Berakhir Seri : ")
                for catur in pertandingan_seri :
                    print("-> " + catur["pemain putih"] + "-" + catur["pemain hitam"])
                print()

            elif input_user == 3 :
                input_pemain = input("Masukkan Nama Pemain : ")

                skor_pemain, ada = poin(pertandingan, input_pemain.lower())

                if ada :
                    print("\n" + "skor " + input_pemain.lower() + " adalah " + str(skor_pemain) + "\n")
                
                else :
                    print("\n" + "Tidak ada pemain bernama " + input_pemain.lower() + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")