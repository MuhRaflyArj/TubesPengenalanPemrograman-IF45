from re import L


def olah_data(isi_data) :
    tabungan = []

    for mahasiswa in isi_data :
        data_mahasiswa = {}
        mahasiswa = mahasiswa.split()

        data_mahasiswa["nama"] = mahasiswa[0]
        data_mahasiswa["harga laptop"] = int(mahasiswa[1])
        data_mahasiswa["tabungan"] = sum([int(i) for i in mahasiswa[2:]])

        tabungan.append(data_mahasiswa)

    return tabungan


def terbanyak(tabungan) :
    tabungan_terbanyak = ""
    nominal_terbanyak = 0

    for mahasiswa in tabungan :
        if mahasiswa["tabungan"] > nominal_terbanyak :
            tabungan_terbanyak = mahasiswa["nama"]
            nominal_terbanyak = mahasiswa["tabungan"]

    return tabungan_terbanyak


def favorit(tabungan) :
    nama_juara = tabungan[0]["nama"]
    selisih_terkecil = tabungan[0]["harga laptop"] - tabungan[0]["tabungan"]

    for mahasiswa in tabungan :
        if mahasiswa["harga laptop"] - mahasiswa["tabungan"] < selisih_terkecil :
            nama_juara = mahasiswa["nama"]
            selisih_terkecil = mahasiswa["harga laptop"] - mahasiswa["tabungan"]

    return nama_juara

    
if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    tabungan = olah_data(isi_data)

    while True :
        try :
            print("1. List Tabungan" + "\n" +
                  "2. Tabungan Terbanyak" + "\n" +
                  "3. Selisih Tabungan Terkecil" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Tabungan Mahasiswa")
                print(tabungan, "\n")

            elif input_user == 2 :
                nama_terbanyak = terbanyak(tabungan)
                print("\n" + "Mahasiswa dengan tabungan terbanyak adalah " + nama_terbanyak + "\n")

            elif input_user == 3 :
                nama_juara = favorit(tabungan)
                print("\n" + "Siswa dengan nominal tabungan paling mendekati harga laptop adalah " + nama_juara + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakash Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")