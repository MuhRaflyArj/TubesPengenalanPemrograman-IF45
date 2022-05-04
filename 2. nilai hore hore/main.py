def olah_data(isi_data) :
    list_data = []

    for baris in isi_data :
        data_siswa = {}
        baris = baris.split()

        data_siswa["nim"] = baris[0]

        for i in range(1, 5) :
            data_siswa[f"clo {i}"] = int(baris[i])

        list_data.append(data_siswa)

    return list_data

def indeks(data_siswa) :

    for i in range(1, 5) :
        if data_siswa[f"clo {i}"] > 80 :
            indeks = "A"
        elif data_siswa[f"clo {i}"] > 70 :
            indeks = "AB"
        elif data_siswa[f"clo {i}"] > 65 :
            indeks = "B"
        elif data_siswa[f"clo {i}"] > 60 :
            indeks = "BC"
        elif data_siswa[f"clo {i}"] > 50 :
            indeks = "C"
        elif data_siswa[f"clo {i}"] > 40 :
            indeks = "D"
        else :
            indeks = "E"

        data_siswa[f"clo {i}"] = indeks

    return data_siswa

def report(data_clo) :
    jumlah_a = 0
    jumlah_ab = 0

    for i in range(len(data_nilai)) :
        data_clo[i] = indeks(data_clo[i])
        list_nilai = [data_clo[i][f"clo {j}"] for j in range(1, 5)]
        
        if "A" in list_nilai :
            jumlah_a += 1
        if "AB" in list_nilai :
            jumlah_ab += 1

    return data_clo, jumlah_a, jumlah_ab

if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    while True :
        try :
            data_nilai = olah_data(isi_data)
            
            print("1. Print Dictionary" + "\n" +
                  "2. Indeks Mahasiswa" + "\n" +
                  "3. List Indeks Mahasiswa" + "\n" +
                  "4. Keluar dari Program")

            input_user = int(input("Masukkan Menu : "))

            if input_user == 1 :
                print("\n" + "Dictionary Data Nilai")
                print(data_nilai, "\n")


            elif input_user == 2 :
                list_nim = [data_siswa["nim"] for data_siswa in data_nilai]
                
                print("\n" + "Daftar NIM")
                for i in range(len(list_nim)) :
                    print(f"{i+1}. {list_nim[i]}")
                input_nim = int(input("Masukkan Menu : "))

                if input_nim < 1 and input_nim > len(list_nim) - 1 :
                    print("\n" + "Input Tidak ada di Menu" + "\n")

                else :
                    data_clo = indeks(data_nilai[input_nim-1])

                    print()
                    for title in data_clo :
                        if title == "nim" :
                            print(title, end="\t\t")
                        else :
                            print(title, end="\t")     
                    print()

                    for nilai in data_clo :
                        print(data_clo[nilai], end="\t")

                    print("\n")


            elif input_user == 3 :
                data_indeks, jumlah_a, jumlah_ab = report(data_nilai)

                print()
                for title in data_nilai[0] :
                    if title == "nim" :
                        print(title, end="\t\t")
                    else :
                        print(title, end="\t")             
                print()

                for i in range(len(data_indeks)) :
                    data_siswa = data_indeks[i]
                    
                    for nilai in data_siswa :
                        print(data_siswa[nilai], end="\t")
                    print()

                print("Jumlah mahasiswa dengan indeks A :", jumlah_a)
                print("Jumlah mahasiswa dengan indeks AB :", jumlah_ab, "\n")
                

            elif input_user == 4 :
                print("\n" + "Terima kasih telah menggunakan program" + "\n")
                exit()


            else :
                print("\n" + "Input Tidak ada di Menu" + "\n")


        except ValueError :
            print("\n" + "Input Salah!!" + "\n")