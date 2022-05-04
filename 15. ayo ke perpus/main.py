def olah_data(isi_data) :
    peminjaman = {}
    data_buku = [buku.split() for buku in isi_data]
    list_hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

    for i in range(1,8) :
        peminjaman[list_hari[i-1]] = sum([int(data_buku[j][i]) for j in range(len(data_buku))])
    
    return peminjaman

def favorit(peminjaman) :
    return max(peminjaman, key=peminjaman.get)

def report(peminjaman, isi_data) :
    for buku in peminjaman :
        peminjaman[buku] = peminjaman[buku]/len(isi_data)

    return peminjaman

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    peminjaman = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Peminjaman" + "\n" +
                  "2. Hari Peminjaman Buku Terbanyak" + "\n" +
                  "3. Rata-Rata Peminjaman Buku" + "\n" +
                  "4. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Peminjaman")
                print(peminjaman, "\n")

            elif input_user == 2 :
                terbanyak = favorit(peminjaman)
                print("\n" + "Peminjaman Buku Terbanyak Terjadi Pada Hari " + terbanyak + "\n")

            elif input_user == 3 :
                rerata = report(peminjaman, isi_data)
                print("\n" + "Rata-Rata Peminjaman")

                for buku in rerata :
                    print(buku + " : " + str(rerata[buku]))
                print()

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")
                print()

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")