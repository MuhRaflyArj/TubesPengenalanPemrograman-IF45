from re import L


def olah_data(isi_data) :
    daftar_poin = {}
    
    for baris in isi_data :
        baris = baris.split()
        skor = baris[2].split("-")

        for i in range(2) :
            if baris[i] not in daftar_poin :
                if skor[i] == "1" :
                    daftar_poin[baris[i]] = 1
                elif skor[i] == "1/2" :
                    daftar_poin[baris[i]] = 0.5
            
            else :
                if skor[i] == "1" :
                    daftar_poin[baris[i]] += 1
                elif skor[i] == "1/2" :
                    daftar_poin[baris[i]] += 0.5

    return daftar_poin

def pemain(daftar_poin) :
    return len(daftar_poin)

def juara(daftar_poin) :
    nama_terbanyak = max(daftar_poin, key=daftar_poin.get)
    skor_terbanyak = daftar_poin[nama_terbanyak]

    return nama_terbanyak, skor_terbanyak


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    

    while True :
        try :
            daftar_poin = olah_data(isi_data)
            
            print("1. Print Dictionary" + "\n" +
                  "2. Banyak Pemain yang Bertanding" + "\n" +
                  "3. Pemain dengan Poin Tertinggi" + "\n" +
                  "4. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Daftar Poin")
                print(daftar_poin, "\n")

            elif input_user == 2 :
                banyak_pemain = str(pemain(daftar_poin))
                print("\n" + "Banyaknya pemain yang bertanding : " + banyak_pemain + "\n")

            elif input_user == 3 :
                nama_terbanyak, skor_terbanyak = juara(daftar_poin)
                print("\n" + "Pemain dengan skor terbanyak adalah " + nama_terbanyak + "\n"
                      "Dengan Skor " + str(skor_terbanyak) + "\n")


            elif input_user == 4 :
                print("\n" + "Terima kasih sudah menggunakan program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")


        except ValueError :
            print("\n" + "Input Salah!!" + "\n")
    