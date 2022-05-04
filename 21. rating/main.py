def olah_data(isi_data) :
    data_mobil = [i.split() for i in isi_data]
    rating = []

    for i in range(len(data_mobil)) :
        data_rating = {}
        data_rating["mobil"] = data_mobil[i][0]

        for j in range(1, len(data_mobil[i])) :
            data_rating[f"spek {j}"] = int(data_mobil[i][j])

        rating.append(data_rating)

    return rating

def terbaik(rating) :
    terbaik = {}
    for i in range(len(rating[0])-1) :
        rating_tertinggi = max([rating[j][f"spek {i+1}"] for j in range(len(rating))])
        terbaik[f"spek {i+1}"] = [rating[j]["mobil"] for j in range(len(rating)) if rating[j][f"spek {i+1}"] == rating_tertinggi]
    
    return terbaik

def report(rating) :
    mobil_terbaik = []

    for i in range(len(rating)) :
        rerata_rating = sum([rating[i][f"spek {j}"] for j in range(1, len(rating[i]))]) / (len(rating[i])-1)
        if rerata_rating > 7 :
            mobil_terbaik.append(rating[i]["mobil"])

    return mobil_terbaik


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    rating = olah_data(isi_data)

    while True :
        try :
            print("1. List Rating" + "\n" +
                  "2. Rating Tertinggi" + "\n" +
                  "3. Rata-Rata Rating" + "\n" +
                  "4. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "List Rating")
                print(rating, "\n")

            elif input_user == 2 :
                spek_terbaik = terbaik(rating)
                print("\n" + "Mobil Dengan Rating Tertinggi di Setiap Spek")

                for i in range(1, len(spek_terbaik)+1) :
                    print(f"spek {i} :", ", ".join(spek_terbaik[f"spek {i}"]))
                print()
        

            elif input_user == 3 :
                mobil_terbaik = report(rating)
                print("\n" + "Mobil Dengan Rating Diatas 7")

                for i in mobil_terbaik :
                    print("->", i)
                print()

            elif input_user == 4 :
                print("\n" + "Terimakasih Telah Mengguakan Program")
                exit()

            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")

        except ValueError :
            print("\n" + "Input Salah!!" + "\n")