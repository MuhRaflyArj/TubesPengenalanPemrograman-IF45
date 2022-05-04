def olah_data(isi_data) :
    data_mahasiswa = [i.split() for i in isi_data]
    tabungan = []

    for mahasiswa in data_mahasiswa :
        data_tabungan = {}

        data_tabungan["nama"] = mahasiswa[0]
        data_tabungan["harga laptop"] = int(mahasiswa[1])
        data_tabungan["tabungan"] = [int(i) for i in mahasiswa[2:]]
        
        tabungan.append(data_tabungan)

    return tabungan

def rerata(data_tabungan) :
    return sum(data_tabungan["tabungan"]) / 4

def tampil_terbanyak(tabungan) :
    daftar_terbanyak = []
    tabungan_mahasiswa = [tabungan[i]["tabungan"] for i in range(len(tabungan))]

    for i in range(4) :
        daftar_perminggu = [tabungan_mahasiswa[j][i] for j in range(len(tabungan_mahasiswa))]
        daftar_terbanyak.append(tabungan[daftar_perminggu.index(max(daftar_perminggu))]["nama"])

    return daftar_terbanyak

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    tabungan = olah_data(isi_data)

    while True :
        try :
            print("1. List Tabungan" + "\n" +
                  "2. Rata-Rata Tabungan Mahasiswa" + "\n" +
                  "3. Tabungan Terbanyak Setiap Minggu" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Tabungan")
                print(tabungan, "\n")

            elif input_user == 2 :
                print("\n" + "Daftar Nama Mahasiswa :")
                for i in range(len(tabungan)) :
                    nama = tabungan[i]["nama"]
                    print(f"{i+1}. {nama}")

                input_daftar_nama = int(input("Masukkan Menu : "))-1

                if input_daftar_nama >= 0 and input_daftar_nama < len(tabungan) :
                     rata_rata = rerata(tabungan[i])
                     print("\n" + f"Rata-Rata tabungan {nama} adalah {rata_rata}" + "\n")
                
                else :
                    print("\n" + "Input Tidak ada di Menu" + "\n")

            elif input_user == 3 :
                daftar_tabungan = tampil_terbanyak(tabungan)
                print("\n" + "Daftar Tabungan Paling Banyak")

                for i in range(len(daftar_tabungan)) :
                    print(f"Minggu ke-{i+1} - {daftar_tabungan[i]}")
                print()


            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + '\n')
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")


    