def olah_data(isi_data) :
    transaksi = {}

    for data_transaksi in isi_data :
        data_transaksi = data_transaksi.replace("/", " ").split()
    
        if f"{data_transaksi[1]}/{data_transaksi[2]}" in list(transaksi.keys()) :
            transaksi[f"{data_transaksi[1]}/{data_transaksi[2]}"] += int(data_transaksi[3])
        else :
            transaksi[f"{data_transaksi[1]}/{data_transaksi[2]}"] = int(data_transaksi[3])
    
    return transaksi

def terendah(transaksi) :
    return [i for i in transaksi if transaksi[i] == min(list(transaksi.values()))]

def report(transaksi) :
    rerata_transaksi = {}

    for data_transaksi in transaksi :
        bulan_transaksi = data_transaksi.split("/")[0]

        if bulan_transaksi in rerata_transaksi :
            rerata_transaksi[bulan_transaksi].append(transaksi[data_transaksi])
        else :
            rerata_transaksi[bulan_transaksi] = [transaksi[data_transaksi]]

    for bulan_transaksi in rerata_transaksi :
        hasil_transaksi = rerata_transaksi[bulan_transaksi]
        rerata_transaksi[bulan_transaksi] = round(sum(hasil_transaksi)/len(hasil_transaksi),2)
    
    return rerata_transaksi
        

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    transaksi = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Transaksi" + "\n" +
                  "2. Transaksi Paling Sedikit" + "\n" +
                  "3. Nilai Rata-Rata Transaksi" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Transaksi")
                print(transaksi, "\n")

            elif input_user == 2 :
                transaksi_terendah = terendah(transaksi)

                print("\n" + "Transaksi Terendah Terjadi Pada Bulan")
                print("\n".join(transaksi_terendah), "\n")


            elif input_user == 3 :
                rerata_transaksi = report(transaksi)
                print("\n" + "Data Rata-Rata Transaksi Setiap Bulan")

                for bulan in rerata_transaksi :
                    print("\t" + f"Rata-Rata Transaksi Bulan {bulan} adalah {rerata_transaksi[bulan]}")
                print()
 
            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")