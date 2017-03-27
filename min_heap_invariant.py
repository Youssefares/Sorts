
def is_min_heap(arr)->bool:
    n = len(arr)
    return all([not (arr[2 * i + 1] < arr[i] or arr[2 * i + 2] < arr[i]) for i in range(n // 2, -1)])