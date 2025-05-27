MAX_BIT = 33
so_cach = [[0] * MAX_BIT for _ in range(MAX_BIT)]

for bit in range(MAX_BIT):
    so_cach[bit][0] = 1

for bit in range(1, MAX_BIT):
    for so_0 in range(1, MAX_BIT):
        if bit < so_0:
            so_cach[bit][so_0] = 0
        else:
            so_cach[bit][so_0] = so_cach[bit - 1][so_0] + so_cach[bit - 1][so_0 - 1]

so_luong_test = int(input())
for _ in range(so_luong_test):
    N, so_bit_0 = map(int, input().split())

    if N == 0:
        print(1 if so_bit_0 == 1 else 0)
        continue

    nhi_phan = bin(N)[2:]
    so_bit = len(nhi_phan)
    ket_qua = 0
    dem_0_truoc = 0

    for i in range(1, so_bit):
        if nhi_phan[i] == '1' and so_bit_0 > dem_0_truoc:
            ket_qua += so_cach[so_bit - i - 1][so_bit_0 - dem_0_truoc - 1]
        if nhi_phan[i] == '0':
            dem_0_truoc += 1

    if dem_0_truoc == so_bit_0:
        ket_qua += 1

    for i in range(so_bit - 1):
        ket_qua += so_cach[i][so_bit_0]

    if so_bit_0 == 1:
        ket_qua += 1

    print(ket_qua)
