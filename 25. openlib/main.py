def olah_data(isi_data) :
    daftar_buku = []

    for buku in isi_data :
        data_buku = {}
        buku = buku.split()

        data_buku["isbn"] = buku[0]
        data_buku["stok"] = int(buku[1])
        data_buku["peminjaman"] = sum([int(i) for i in buku[2:]])

        daftar_buku.append(data_buku)

    return daftar_buku

def terbanyak(daftar_buku) :
    peminjaman_terbanyak = max([i["peminjaman"] for i in daftar_buku])

    return [i["isbn"] for i in daftar_buku if i["peminjaman"] == peminjaman_terbanyak]

def report(daftar_buku) :
    rerata_peminjaman = []

    for buku in daftar_buku :
        data_buku = {}
        
        data_buku["isbn"] = buku["isbn"]
        data_buku["rerata"] = round(buku["peminjaman"] / 6, 2)

        rerata_peminjaman.append(data_buku)

    return rerata_peminjaman


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    daftar_buku = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Daftar Buku" + "\n" +
                  "2. Peminjaman Terbanyak" + "\n" +
                  "3. Rata-Rata Peminjaman" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Daftar Buku")
                print(daftar_buku, "\n")

            elif input_user == 2 :
                peminjaman_terbanyak = terbanyak(daftar_buku)
                print("\n" + "ISBN Buku Peminjaman Terbanyak Adalah" + "\n" +'\n'.join(peminjaman_terbanyak), "\n")

            elif input_user == 3 :
                rerata_peminjaman = report(daftar_buku)
                print("\n" + "Data Rerata Peminjaman")

                for buku in rerata_peminjaman :
                    isbn, rerata = buku["isbn"], buku["rerata"]
                    print("\t" + f"Buku {isbn} memiliki rerata peminjaman sebanyak {rerata}")
                print()

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")