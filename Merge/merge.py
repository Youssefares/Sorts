def merge(a, aux, lo:int, mid: int, hi:int):

    #TODO: can we get rid of this?
    for i in range(lo, hi+1):
        aux[i] = a[i]

    i = lo
    j = mid+1
    for k in range(lo, hi+1):
        #if exhausted first half
        if i > mid:
            a[k] = aux[j]
            j += 1
        #else if exhausted second half
        elif j > hi:
            a[k] = aux[i]
            i += 1
        #else compare and add
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1
