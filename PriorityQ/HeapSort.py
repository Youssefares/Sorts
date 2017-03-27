from PriorityQ.min_heap import MinHeap


def heap_sort(arr):
    heap = MinHeap(arr)
    new_arr =[]
    while len(heap.arr) > 0:
        new_arr.append(heap.delete_min())
    arr.extend(new_arr)
