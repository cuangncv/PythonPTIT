def xac_dinh_cung(ngay, thang):
    if (thang == 1 and ngay >= 20) or (thang == 2 and ngay <= 18):
        return "Bao Binh"
    elif (thang == 2 and ngay >= 19) or (thang == 3 and ngay <= 20):
        return "Song Ngu"
    elif (thang == 3 and ngay >= 21) or (thang == 4 and ngay <= 19):
        return "Bach Duong"
    elif (thang == 4 and ngay >= 20) or (thang == 5 and ngay <= 20):
        return "Kim Nguu"
    elif (thang == 5 and ngay >= 21) or (thang == 6 and ngay <= 20):
        return "Song Tu"
    elif (thang == 6 and ngay >= 21) or (thang == 7 and ngay <= 22):
        return "Cu Giai"
    elif (thang == 7 and ngay >= 23) or (thang == 8 and ngay <= 22):
        return "Su Tu"
    elif (thang == 8 and ngay >= 23) or (thang == 9 and ngay <= 22):
        return "Xu Nu"
    elif (thang == 9 and ngay >= 23) or (thang == 10 and ngay <= 22):
        return "Thien Binh"
    elif (thang == 10 and ngay >= 23) or (thang == 11 and ngay <= 22):
        return "Thien Yet"
    elif (thang == 11 and ngay >= 23) or (thang == 12 and ngay <= 21):
        return "Nhan Ma"
    elif (thang == 12 and ngay >= 22) or (thang == 1 and ngay <= 19):
        return "Ma Ket"

test = int(input())
for i in range (test):
    a , b = map(int, input().split())
    print(xac_dinh_cung(a,b))