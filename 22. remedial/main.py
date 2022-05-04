def olah_data(isi_data) :
    daftar_nilai = [i.split() for i in isi_data]
    daftar_clo = {}

    for i in range(len(daftar_nilai)) :
        daftar_clo[daftar_nilai[i][0]] = [int(i) for i in daftar_nilai[i][1:]]

    return daftar_clo

def remedial_report(daftar_clo) :
    daftar_remedial = {}
    for nim in daftar_clo :
        for i in range(len(daftar_clo[nim])) :
            if daftar_clo[nim][i] < 50 :
                if nim in daftar_remedial :
                    daftar_remedial[nim] += f", clo {i+1}"
                else :
                    daftar_remedial[nim] = f"clo {i+1}"
    
    return daftar_remedial

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    daftar_clo = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary daftar_clo" + "\n" +
                  "2. Daftar Remedial Siswa" + "\n" +
                  "3. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary daftar_clo")
                print(daftar_clo, "\n")

            elif input_user == 2 :
                print("\n" + "Daftar Remedial")
                data_remedial = daftar_clo
                daftar_remedial = remedial_report(data_remedial)

                for nim in daftar_remedial :
                    print(nim, "->", daftar_remedial[nim])
                print()


            elif input_user == 3 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")