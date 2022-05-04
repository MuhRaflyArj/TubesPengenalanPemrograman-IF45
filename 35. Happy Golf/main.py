def olah_data(isi_data) :
    skor = {"QD" : 4, "TP" : 3, "DB" : 2, "BG" : 1, "PAR" : 0, "BR" : -1, "EG" : -2, "AL" : -3, "CN" : -4}
    data_pemain = [i.split() for i in isi_data]
    pemain_golf = []

    for i in range(len(data_pemain)) :
        data = {"nama" : data_pemain[i][0], "skor" : 0}

        for j in range(1, len(data_pemain[i])) :
            if data_pemain[i][j] in list(skor.keys()) :
                data["skor"] += skor[data_pemain[i][j]]+5

        pemain_golf.append(data)
    
    return pemain_golf

def pemenang(pemain_golf) :
    return [pemain["nama"] for pemain in pemain_golf if pemain["skor"] == min([i["skor"] for i in pemain_golf])][0]

def rerata(pemain_golf) :
    return [{"nama" : pemain["nama"], "rerata" : round(pemain["skor"]/18, 2)} for pemain in pemain_golf]

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    pemain_golf = olah_data(isi_data)

    while True :
        try :
            print("1. List Pemain Golf" + "\n" +
                  "2. Pemenang" + "\n" +
                  "3. Rata-Rata Skor Pemain" +'\n' +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Pemain Golf")
                print(pemain_golf, "\n")

            elif input_user == 2 :
                nama_pemenang = pemenang(pemain_golf)
                print("\n" + f"Pemenang Adalah {nama_pemenang}" + "\n")

            elif input_user == 3 :
                rerata_pemain = rerata(pemain_golf)
                print("\n" + "Data Rerata Pemain Golf")

                for pemain in rerata_pemain :
                    nama, skor_rerata = pemain["nama"], pemain["rerata"]
                    print("-> " + f"Rerata {nama} adalah {skor_rerata}")
                print()

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")