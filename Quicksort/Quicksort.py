def quicksort(arr, left, right):
    if left >= right:
        return

    # TODO: smarter way to choose pivot?
    mid = (left + right) // 2
    pivot = arr[mid]
    split = partn(arr, left, right, pivot)
    quicksort(arr, left, split - 1)
    quicksort(arr, split, right)

# TODO: rename function
def partn(arr, left, right, pivot):

    while left <= right:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left] # swap elements
            left += 1
            right -= 1

    return left


# Test
arr = [2, 8, 7, 1, 3, 5, 6, 4]
print("Array before sorting: {}".format(arr))
quicksort(arr, 0, len(arr) - 1)
print("Array after sorting: {}".format(arr))
