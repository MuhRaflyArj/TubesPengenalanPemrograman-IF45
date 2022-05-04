def olah_data(isi_data) :
    data_kamus = [i.split() for i in isi_data]
    kamus = {}

    for data in data_kamus :
        kamus[data[0]] = {"en" : data[1], "su" : data[2], "ja" : data[3]}

    return kamus

def id_to_en(kamus) :
    kamus_id_to_en = {}

    for kata in kamus :
        kamus_id_to_en[kata] = kamus[kata]["en"]

    return kamus_id_to_en

def id_to_su(kamus) :
    kamus_id_to_su = {}

    for kata in kamus :
        kamus_id_to_su[kata] = kamus[kata]["su"]

    return kamus_id_to_su

def id_to_ja(kamus) :
    kamus_id_to_ja = {}

    for kata in kamus :
        kamus_id_to_ja[kata] = kamus[kata]["ja"]

    return kamus_id_to_ja

def su_to_ja(kamus) :
    kamus_su_to_ja = {} 

    for kata in kamus :
        kamus_su_to_ja[kamus[kata]["su"]] = kamus[kata]["ja"]

    return kamus_su_to_ja

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    kamus = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Kamus" + "\n" +
                  "2. Translate Indonesia ke Inggris" + "\n" +
                  "3. Translate Indonesia ke Sunda" + "\n" +
                  "4. Transalte Indonesia ke Jawa" + "\n" +
                  "5. Translate Sunda ke Jawa" + "\n" +
                  "6. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Kamus")
                print(kamus, "\n")

            elif input_user == 2 :
                translate_id_to_en = id_to_en(kamus)
                print("\n" + "Translate Indonesia ke Inggris")

                for kata in translate_id_to_en :
                    print(f"{kata} : {translate_id_to_en[kata]}")
                print()

            elif input_user == 3 :
                translate_id_to_su = id_to_su(kamus)
                print("\n" + "Translate Indonesia ke Sunda")


                for kata in translate_id_to_su :
                    print(f"{kata} : {translate_id_to_su[kata]}")
                print()

            elif input_user == 4 :
                translate_id_to_ja = id_to_ja(kamus)
                print("\n" + "Translate Indonesia ke Jawa")

                for kata in translate_id_to_ja :
                    print(f"{kata} : {translate_id_to_ja[kata]}")
                print()

            elif input_user == 5 :
                translate_su_to_ja = su_to_ja(kamus)
                print("\n" + "Translate Sunda ke Jawa")

                for kata in translate_su_to_ja :
                    print(f"{kata} : {translate_su_to_ja[kata]}")
                print()

            elif input_user == 6 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")