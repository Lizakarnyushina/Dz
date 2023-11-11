def binary_search(x, y):
    low = 0
    high = len(x) - 1
    result = None

    while low <= high:
        mid = (low + high) // 2
        if x[mid] >= y:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result