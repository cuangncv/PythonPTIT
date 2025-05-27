INF = 10 ** 18


def read_valid_list(n):
    """Đọc danh sách sở thích và lọc các chỉ số hợp lệ"""
    _ = int(input())  # số lượng không cần thiết vì ta sẽ lọc lại
    lst = list(map(int, input().split()))
    return [i for i in lst if 0 < i <= n]


def select_items(sorted_list, count, cost_array, selected, mark_shared=False, reduce_other=None):
    """Chọn 'count' món rẻ nhất từ sorted_list, tránh trùng món đã chọn"""
    total = 0
    taken = 0
    for item in sorted_list:
        if taken >= count:
            break
        if item in selected:
            continue
        total += cost_array[item]
        selected.add(item)
        if mark_shared:
            cost_array[item] = -1
        else:
            cost_array[item] = -INF
        if reduce_other is not None and item in reduce_other:
            reduce_other[item] -= 1
        taken += 1
    return total, taken


def solve():
    n, m, k = map(int, input().split())
    costs = [0] + list(map(int, input().split()))

    ti_likes = read_valid_list(n)
    teo_likes = read_valid_list(n)

    if m < k or m > n or k > len(ti_likes) or k > len(teo_likes):
        print(-1)
        return

    shared_likes = sorted(set(ti_likes) & set(teo_likes), key=lambda i: costs[i])
    ti_likes_sorted = sorted(ti_likes, key=lambda i: costs[i])
    teo_likes_sorted = sorted(teo_likes, key=lambda i: costs[i])

    min_shared_required = max(0, 2 * k - m)
    if len(shared_likes) < min_shared_required:
        print(-1)
        return

    selected_items = set()
    total_cost = 0

    # Bước 1: chọn các món chung bắt buộc
    shared_mark = {i: True for i in shared_likes}
    total_cost += sum(costs[item] for item in shared_likes[:min_shared_required])
    for item in shared_likes[:min_shared_required]:
        selected_items.add(item)
        costs[item] = -1
    m -= min_shared_required
    k_remaining_ti = k - min_shared_required
    k_remaining_teo = k - min_shared_required

    # Bước 2: chọn thêm cho Tí
    for item in ti_likes_sorted:
        if k_remaining_ti == 0:
            break
        if item in selected_items:
            continue
        total_cost += costs[item]
        selected_items.add(item)
        if item in shared_mark:
            k_remaining_teo -= 1
        costs[item] = -INF
        k_remaining_ti -= 1
        m -= 1

    # Bước 3: chọn thêm cho Tèo
    for item in teo_likes_sorted:
        if k_remaining_teo == 0:
            break
        if item in selected_items:
            continue
        total_cost += costs[item]
        selected_items.add(item)
        costs[item] = -INF
        k_remaining_teo -= 1
        m -= 1

    if k_remaining_ti > 0 or k_remaining_teo > 0:
        print(-1)
        return

    # Bước 4: chọn thêm các món rẻ nhất còn lại để đủ m món
    remaining = sorted((costs[i], i) for i in range(1, n + 1) if i not in selected_items)
    for cost, idx in remaining:
        if m == 0:
            break
        total_cost += cost
        m -= 1

    print(-1 if m > 0 else total_cost)


solve()
