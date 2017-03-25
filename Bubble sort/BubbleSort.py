def bubble_sort(arr):

    for j in range(len(arr)-1):
        last = len(arr)-j-1
        for i in range(last):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]  # swap
