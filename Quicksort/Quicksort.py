from Quicksort import KnuthShuffle


def quicksort(arr):
    KnuthShuffle.knuth_shuffle(arr)
    run_quicksort(arr, 0, len(arr) - 1)


def run_quicksort(arr, left, right):
    if left >= right:
        return
    split = partn(arr, left, right)
    run_quicksort(arr, left, split - 1)
    run_quicksort(arr, split + 1, right)


def partn(arr, left, right):
    pivot = arr[left]
    i = left + 1
    j = right
    while True:
        while arr[i] < pivot and i < right:
            i += 1

        while arr[j] > pivot and j > left:
            j -= 1

        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i] # swap elements
        i += 1
        j -= 1

    arr[left], arr[j] = arr[j], arr[left]
    return j

