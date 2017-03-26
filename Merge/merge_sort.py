from Merge.merge import merge

sentinel = object()
def merge_sort(a, aux=sentinel, lo:int=0, hi:int=sentinel):
    #just initializing hi for the 1st callback
    if hi is sentinel:
        hi = len(a)-1
    if aux is sentinel:
        aux = [None] * (hi+1)

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
