def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def stalin_sort(arr):
    sorted_arr = [arr[0]]
    for num in arr[1:]:
        if num >= sorted_arr[-1]:
            sorted_arr.append(num)
    return sorted_arr


def sleep_sort(input_list):
    import time
    sorted_list = []

    def add_to_sorted_list(x):
        time.sleep(x)
        sorted_list.append(x)

    for num in input_list:
        add_to_sorted_list(num)

    return sorted_list
