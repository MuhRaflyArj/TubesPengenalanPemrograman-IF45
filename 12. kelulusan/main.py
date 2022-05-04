def olah_data(isi_data) :
    # 1. rerata , 2. tertinggi, 3 terendah, 4 <= 50
    daftar_clo = {}

    data_clo = [clo.split() for clo in isi_data]

    for i in range(1, 5) :
        daftar_clo[f"clo {i}"] = [0 for i in range(4)]

        daftar_clo[f"clo {i}"][0] = round(sum([int(data_clo[j][i]) for j in range(len(data_clo))]) / len(data_clo), 2) 
        daftar_clo[f"clo {i}"][1] = max([int(data_clo[j][i]) for j in range(len(data_clo))])
        daftar_clo[f"clo {i}"][2] = min([int(data_clo[j][i]) for j in range(len(data_clo))])
        daftar_clo[f"clo {i}"][3] = len([int(data_clo[j][i]) for j in range(len(data_clo)) if int(data_clo[j][i]) <= 50])

    return daftar_clo


def report(daftar_clo) :
    rerata = [daftar_clo[f"clo {i}"][0] for i in range(1, 5)]
    tertinggi = [daftar_clo[f"clo {i}"][1] for i in range(1, 5)]
    terendah = [daftar_clo[f"clo {i}"][2] for i in range(1, 5)]
    remedial = [daftar_clo[f"clo {i}"][3] for i in range(1, 5)]

    return rerata, tertinggi, terendah, remedial

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    daftar_clo = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Daftar CLO" + "\n" +
                  "2. Data Setiap CLO" + "\n" +
                  "3. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Daftar CLO")
                print(daftar_clo, "\n")

            elif input_user == 2 :
                
                rerata, tertinggi, terendah, remedial = report(daftar_clo)
                print("\n" + f"           CLO 1   CLO 2   CLO 3   CLO 4")
                print(f"rerata     {rerata[0]}   {rerata[1]}   {rerata[2]}   {rerata[3]}")
                print(f"tertinggi  {tertinggi[0]}     {tertinggi[1]}      {tertinggi[2]}      {tertinggi[3]}")
                print(f"terendah   {terendah[0]}     {terendah[1]}      {terendah[2]}      {terendah[3]}")
                print(f"remedial    {remedial[0]}      {remedial[1]}       {remedial[2]}       {remedial[3]}" + "\n")

            elif input_user == 3 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")


        except ValueError :
            print("\n" + "Input Salah!!" + "\n")

