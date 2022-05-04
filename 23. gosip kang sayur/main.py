def olah_data(isi_data) :
    rumah_ganjil, rumah_genap = {}, {}

    for i in range(len(isi_data)-1) :
        isi_data[i] = isi_data[i].replace(" \n", "")
    
    no_rumah, panjang_rumah = int(isi_data[0].split()[0]), int(isi_data[0].split()[1])

    for i in range(1, panjang_rumah+1) :
        if i % 2 == 0 :
            rumah_genap[i] = ""
        else :
            rumah_ganjil[i] = ""
    
    if no_rumah % 2 == 0 :
        rumah_genap[no_rumah] = "anda"
    else :
        rumah_ganjil[no_rumah] = "anda"

    for gosip in isi_data[1:] :
        gosip = gosip.split()

        pergeseran, sisi, arah, rumah_patokan, rumah_baru = int(gosip[0]), gosip[2], gosip[3], gosip[5], gosip[-1]

        if rumah_patokan in list(rumah_genap.values()) :
            for nomor in rumah_genap :
                if rumah_genap[nomor] == rumah_patokan :
                    nomor_rumah = nomor
        elif rumah_patokan in list(rumah_ganjil.values()) :
            for nomor in rumah_ganjil :
                if rumah_ganjil[nomor] == rumah_patokan :
                    nomor_rumah = nomor

        if sisi == "sebelah" and arah == "kanan":
            pergeseran = pergeseran*2 
        elif sisi == "sebelah" and arah == "kiri" :
            pergeseran = pergeseran*-2
        elif sisi == "seberang" and arah == "kiri":
            if nomor_rumah % 2 == 0 :
                pergeseran = (pergeseran*2 + 1) * -1
            else :
                pergeseran = pergeseran*-2 + 1
        elif sisi == "seberang" and arah == "kanan" :
            pergeseran = pergeseran*2
        
        nomor_baru = nomor_rumah + pergeseran

        if nomor_baru % 2 == 0 :
            rumah_genap[nomor_baru] = rumah_baru
        else :
            rumah_ganjil[nomor_baru] = rumah_baru

    return rumah_ganjil, rumah_genap

def nomor_rumah(rumah_ganjil, rumah_genap, penghuni) :
    if penghuni in list(rumah_genap.values()) :
        for nomor in rumah_genap :
            if rumah_genap[nomor] == penghuni :
                return nomor

    elif penghuni in list(rumah_ganjil.values()) :
        for nomor in rumah_ganjil :
            if rumah_ganjil[nomor] == penghuni :
                return nomor
                
    else :
        return "tidak tahu"

def penghuni_rumah(rumah_ganjil, rumah_genap, nomor) :
    penghuni = ""
    if nomor % 2 == 0 :
        penghuni = rumah_genap[nomor]
    else :
        penghuni = rumah_ganjil[nomor]

    if penghuni == "" :
        return "tidak tahu"
    else :
        return penghuni  

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    rumah_ganjil, rumah_genap = olah_data(isi_data)

    while True :
        try :
            print("1. Dictionary Rumah Ganjil dan Rumah Genap" + "\n" +
                  "2. Cari Nama Keluarga" + "\n" +
                  "3. Cari Nomor Rumah" + "\n" +
                  "4. Keluar Dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Rumah Ganjil")
                print(rumah_ganjil)
                print("\n" + "Dictionary Rumah Genap")
                print(rumah_genap, "\n")

            elif input_user == 2 :
                print("\n" + "Cari nomor rumah")

                input_nama = input("Masukkan nama keluarga : ").capitalize()
                nomor = nomor_rumah(rumah_ganjil, rumah_genap, input_nama)

                if nomor == "tidak tahu" :
                    print("\n" + "tidak tahu" + "\n")
                else :
                    print("\n" + f"{input_nama} tinggal di rumah nomor {nomor}" + "\n")

            elif input_user == 3 :
                print("\n" + "Cari nama penghuni")

                input_nomor = int(input("Masukkan nomor rumah : "))
                penghuni = penghuni_rumah(rumah_ganjil, rumah_genap, input_nomor)

                if penghuni == "tidak tahu" :
                    print("\n" + "tidak tahu" + "\n")
                else :
                    print("\n" + f"{penghuni} tinggal di nomor {input_nomor}" + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")