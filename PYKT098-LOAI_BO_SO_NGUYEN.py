def should_keep(s):
    try:
        k = int(s)
        # loại số nếu nó nhỏ hơn hoặc bằng 64-bit
        return k > (1 << 63) or k < -(1 << 63)
    except:
        return True  # giữ lại nếu không ép được sang int (tức là chữ)

words = []

with open('DATA.in', 'r') as file:
    for line in file:
        tokens = line.strip().split()
        for token in tokens:
            if should_keep(token):
                words.append(token)

words.sort()
print(' '.join(words))