def knuth_shuffle(arr):
    import random
    for i in range(len(arr)):
        rind = random.randrange(i+1)
        arr[rind], arr[i] = arr[i], arr[rind]
