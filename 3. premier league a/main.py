def olah_data(isi_data) :
    klasemen = {}

    for pertandingan in isi_data :
        pertandingan = pertandingan.split()
        tim_1, tim_2 = pertandingan[0], pertandingan[3]

        
        if tim_1 not in klasemen :
            klasemen[tim_1] = [0 for i in range(8)]
        if tim_2 not in klasemen :
            klasemen[tim_2] = [0 for i in range(8)]

        skor_1, skor_2 = int(pertandingan[1]), int(pertandingan[2])
        klasemen[tim_1][0] += 1
        klasemen[tim_2][0] += 1

        klasemen[tim_1][4] += skor_1
        klasemen[tim_1][5] += skor_2

        klasemen[tim_2][4] += skor_2
        klasemen[tim_2][5] += skor_1

        if skor_1 > skor_2 :
            klasemen[tim_1][1] += 1
            klasemen[tim_2][3] += 1

        elif skor_1 == skor_2 :
            klasemen[tim_1][2] += 1
            klasemen[tim_2][2] += 1

        else :
            klasemen[tim_1][3] += 1
            klasemen[tim_2][1] += 1

    for tim in klasemen :
        klasemen[tim][6] = klasemen[tim][4] - klasemen[tim][5]

        klasemen[tim][7] = 3*klasemen[tim][1] + klasemen[tim][2]

    return klasemen


if __name__ == "__main__" :
    data = open("data.txt", "r")
    isi_data = data.readlines()
    data.close()

    klasemen = olah_data(isi_data)
    
    print('%-16s %-8s %-8s %-8s %-8s %-8s %-8s %-12s %-8s' %('Nama Tim', 'Main', 'Menang', 'Draw', 'Kalah', 'Gol', 'Kebobolan', 'Selisih', 'Poin'))

    for tim in klasemen : 
        data_tim = klasemen[tim]              
        print('%-16s %-8s %-8s %-8s %-8s %-8s %-8s %-12s %-8s' %(tim, data_tim[0], data_tim[1], data_tim[2], data_tim[3], data_tim[4], data_tim[5], data_tim[6], data_tim[7]))
