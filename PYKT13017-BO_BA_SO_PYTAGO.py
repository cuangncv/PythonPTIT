def luy_thua(p, e):
    if e == 0: return 1
    if e % 2 == 1: return luy_thua(p, e - 1) * p
    giua = luy_thua(p, e // 2)
    return giua * giua

def so_cap_pytago_luy_thua(p, e):
    modulo = luy_thua(p, e)
    dem = 0
    so_binh_phuong = [0] * modulo

    # Đếm số lần mỗi giá trị bình phương mod P xuất hiện
    for i in range(modulo):
        so_binh_phuong[i * i % modulo] += 1

    # Đếm số bộ (a^2 + b^2 ≡ c^2)
    for i in range(modulo):
        dem += so_binh_phuong[i] * so_binh_phuong[(i + 1) % modulo]

    # Xử lý các trường hợp đặc biệt theo từng bội của p
    for i in range(0, modulo, p):
        binh = i * i % modulo
        dem += so_binh_phuong[(binh + 1) % modulo]

    dem *= (modulo // p) * (p - 1)

    if e > 1:
        dem += so_cap_pytago_luy_thua(p, e - 2) * p * p * p
    else:
        dem += 1

    return dem

def tru_so_0(modulo):
    dem = 1 + 3 * danh_dau_binh_phuong[0]
    for i in range(modulo):
        dem += danh_dau_binh_phuong[i] * (2 * danh_dau_binh_phuong[i] + danh_dau_binh_phuong[(modulo - i) % modulo])
    return dem

def tinh_duong_cheo(modulo):
    dem = 0
    for i in range(1, modulo):
        dem += danh_dau_binh_phuong[2 * i * i % modulo]
    return dem

# Nhập vào N
N = int(input())
danh_dau_binh_phuong = [0] * N
goc_N = N
ket_qua = 1
p = 2

# Phân tích thừa số nguyên tố của N
while p * p <= N:
    if N % p == 0:
        mu = 0
        while N % p == 0:
            mu += 1
            N //= p
        ket_qua *= so_cap_pytago_luy_thua(p, mu)
    p += 1

if N != 1:
    ket_qua *= so_cap_pytago_luy_thua(N, 1)

# Đếm số bình phương mod goc_N
danh_dau_binh_phuong = [0] * goc_N
for i in range(1, goc_N):
    danh_dau_binh_phuong[i * i % goc_N] += 1

# Trừ số bộ ba không hợp lệ
ket_qua -= tru_so_0(goc_N)
ket_qua += tinh_duong_cheo(goc_N)

# Kết quả chia đôi vì mỗi bộ (a, b, c) và (b, a, c) được đếm hai lần nếu a ≠ b
print(ket_qua // 2)
