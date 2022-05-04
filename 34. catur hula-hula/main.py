def olah_data(isi_data) :
    peta_catur = [[] for i in range(8)]

    for i in range(len(isi_data)) :
        for item in isi_data[i] :
            if item.isdigit() :
                peta_catur[i].extend([" " for a in range(int(item))])
            else :
                peta_catur[i].append(item)

    return peta_catur[::-1]

def nilai_buah(posisi) :
    skor = {"k":200,"q":9,"r":5,"b":3,"n":3,"p":1}

    skor_putih, skor_hitam = 0, 0

    for baris in posisi :
        for kolom in baris :
            if kolom != " " and kolom.isupper() :
                skor_putih += skor[kolom.lower()]

            elif kolom != " " and kolom.islower() :
                skor_hitam += skor[kolom]

    return skor_putih, skor_hitam


def posisi_bidak(posisi) :
    posisi, koordinat_bidak = posisi[::-1], []

    for i in range(len(posisi)) :
        for j in range(len(posisi[i])) :
            if posisi[i][j] != " " :
                koordinat = f"{posisi[i][j]} : {chr(97+i)}{j+1}"
                koordinat_bidak.append(koordinat)

    return koordinat_bidak

def jumlah_petak_kosong(posisi) :
    jumlah_kosong = 0
    
    for baris in posisi :
        jumlah_kosong += ''.join(baris).count(" ")

    return jumlah_kosong



if __name__ == "__main__" :
    data = open("data1.txt", "r")
    isi_data = data.read().split("/")
    data.close()

    posisi = olah_data(isi_data)

    while True :
        try :
            print("1. List Posisi" + "\n" +
                  "2. Skor Bidak Pemain" + "\n" +
                  "3. Jumlah Petak Kosong" + "\n" +
                  "4. Koordinat Catur" + "\n" +
                  "5. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Posisi")
                for baris in posisi :
                    print(baris)
                print()

            elif input_user == 2 :
                skor_putih, skor_hitam = nilai_buah(posisi)

                print("\n" + "1. Skor Pemain Putih" + "\n" +
                      "2. Skor Pemain Hitam")

                input_skor = int(input("Masukkan Menu : "))
                
                if input_skor == 1 :
                    print("\n" + f"Skor Pemain Putih Adalah {skor_putih}" + "\n")
                elif input_skor == 2 :
                    print("\n" + f"Skor Pemain Hitam Adalah {skor_hitam}" + "\n")
                else :
                    print("\n" + "Input Tidak ada di Menu" + "\n")

            elif input_user == 3 :
                jumlah_kosong = jumlah_petak_kosong(posisi)  

                print("\n" + f"Jumlah Petak Kosong Pada Papan Catur Adalah {jumlah_kosong}" + "\n")

            elif input_user == 4 :
                koordinat_bidak = posisi_bidak(posisi)

                print("\n" + "Koordinat Bidak Sebagai Berikut" + "\n\t" + "\n\t".join(koordinat_bidak) + "\n")

            elif input_user == 5 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")
            

            
