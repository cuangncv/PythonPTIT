def band_score(d):
    score_ranges = [
        (4, 2.5), (6, 3.0), (9, 3.5), (12, 4.0), (15, 4.5),
        (19, 5.0), (22, 5.5), (26, 6.0), (29, 6.5), (32, 7.0),
        (34, 7.5), (36, 8.0), (38, 8.5), (40, 9.0)
    ]
    return next(score for max_score, score in score_ranges if d <= max_score)
def overall (score):
    s = score - int(score)
    if s < 0.25:
        return int(score)
    elif s < 0.75:
        return int(score) + 0.5
    else:
        return int(score) + 1
for i in range (int(input())):
    diem = list(map(float, input().split()))
    d1, d2, d3, d4 = band_score(diem[0]), band_score(diem[1]), diem[2], diem[3]
    print("{:.1f}".format(overall((d1 + d2 + d3 + d4) / 4)))
