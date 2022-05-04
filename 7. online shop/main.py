def olah_data(isi_data) :
    daftar_user = []

    for user in isi_data :
        data_user = {}
        user = user.split("$")

        data_user["user_id"] = user[0]
        data_user["nama pelanggan"] = user[1]
        data_user["tanggal daftar"] = user[2]
        data_user["tanggal lahir"] = user[3].replace(" \n", "")

        daftar_user.append(data_user)

    return daftar_user

def report(daftar_user, bulan) :
    list_nama = []

    for user in daftar_user :
        if user["tanggal daftar"].split()[1].lower() == bulan.lower() :
            list_nama.append(user["nama pelanggan"])

    return list_nama

def termuda(daftar_user) :
    user_termuda = ""
    tahun_termuda = 0

    for user in daftar_user :
        if int(user["tanggal lahir"].split()[2]) > tahun_termuda :
            user_termuda = user["nama pelanggan"]
            tahun_termuda = int(user["tanggal lahir"].split()[2])

    return user_termuda


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    daftar_user = olah_data(isi_data)

    while True :
        try :
            print("1. List Daftar User" + "\n" +
                  "2. Cari Pendaftar pada Bulan" + "\n" +
                  "3. User Termuda" + "\n" +
                  "4. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Daftar User")
                print(daftar_user, "\n")

            elif input_user == 2 :
                input_bulan = input("\nMasukkan Bulan : ")

                list_pendaftar = report(daftar_user, input_bulan)

                if len(list_pendaftar) > 0 :
                    print("\n" + f"User Yang Lahir Pada Bulan {input_bulan.capitalize()}")
                    
                    for user in list_pendaftar :
                        print("-> " + user)
                    print()

                else :
                    print("\n" + f"Tidak Ada User Yang Lahir di Bulan {input_bulan.capitalize()}" + "\n")


            elif input_user == 3 :
                user_termuda = termuda(daftar_user)

                print("\n" + f"{user_termuda} Merupakan User Termuda" + "\n")

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Menggunakan Program" + "\n")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")

