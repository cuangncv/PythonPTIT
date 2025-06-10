import re

s = ""
while True:
    try:
        s += input() + " "
    except EOFError:
        break

r = re.split(r'[.?!]+', s)
for l in r:
    words = l.split()
    if words:
        words = [w.lower() for w in words]
        words[0] = words[0].capitalize()
        print(*words)
    print()