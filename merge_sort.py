from is_sorted import is_sorted

sentinel = object()
def merge_sort(a:[int], aux:[int]=None, lo:int=0, hi:int=sentinel):
    #just initializing hi for the 1st callback
    if hi is sentinel:
        hi = len(a)-1

    #Base case
    if hi <= lo:
        return

    mid = (lo+hi)//2
    #sort left half
    merge_sort(a, aux, lo, mid)
    #sort right half
    merge_sort(a, aux, mid+1, hi)

    #if things are out of order, merge..
    #else nothing to be done.
    if a[mid+1] < a[mid]:
        merge(a, aux, lo, mid, hi)

#TODO: can we modify this so that it doesn't move so much data arround
def merge(a:[int], aux:[int], lo:int, mid:int, hi:int):
    assert is_sorted(a, lo, mid)
    assert is_sorted(a, mid+1, hi)

    #TODO: can we get rid of this?
    aux = list(a)


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
