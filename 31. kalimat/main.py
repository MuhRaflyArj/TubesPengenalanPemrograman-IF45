def jumlah_num(kalimat) :
    total = 0

    for baris in kalimat :
        for i in range(baris.count("Rp")) :

            total += int(baris[baris.index("Rp")+1].replace(".", "").replace(",", ""))
            baris.pop(baris.index("Rp")+1); baris.pop(baris.index("Rp"))
    
    return total
        
def frekuensi_tinggi(kalimat) :
    frekuensi_kalimat = {}

    for baris in kalimat :
        for kata in baris :
            if kata != "Rp" :
                if kata not in list(frekuensi_kalimat.keys()) :
                    frekuensi_kalimat[kata] = 1

                elif kata in list(frekuensi_kalimat.keys()) :
                    frekuensi_kalimat[kata] += 1

    return [kata for kata in frekuensi_kalimat if frekuensi_kalimat[kata] == max(list(frekuensi_kalimat.values()))]

def kata_berawalan(kalimat, huruf) :
    berawalan_huruf = []

    for baris in kalimat :
        berawalan_huruf.extend([kata.lower() for kata in baris if kata[0].lower() == huruf])

    return list(set(berawalan_huruf))

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    kalimat = [i.split() for i in isi_data]

    while True :
        try :
            print("1. List Kalimat" + "\n" +
                  "2. Penjumlahan Karakter Numerik" + "\n" +
                  "3. Kata Yang Paling Banyak Muncul" + "\n" +
                  "4. Cari Kata" + "\n" +
                  "5. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Kalimat")
                print(kalimat, "\n")

            elif input_user == 2 :
                total_numerik = jumlah_num(kalimat)
                print("\n" + f"Total Penjumlahan Karakter Numerik Pada String Adalah {total_numerik}" + "\n")

            elif input_user == 3 :
                kata_terbanyak = frekuensi_tinggi(kalimat)
                print("\n" + "Kata Terbanyak Pada String Adalah " + ", ".join(kata_terbanyak) + "\n")

            elif input_user == 4 :
                input_huruf = input("\n" + "Masukkan Huruf : ").lower()

                kata_dicari = kata_berawalan(kalimat, input_huruf)

                if len(kata_dicari) > 0 :
                    print("\n" + f"Berikut Kata Awalan Yang Berawal Dari {input_huruf}")

                    for kata in kata_dicari :
                        print("-> " + kata)
                    print()
                    
                else :
                    print("\n" + f"Tidak Ada Kata Yang Berawalan Dari {input_huruf}" + "\n")

            elif input_user == 5 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")
                