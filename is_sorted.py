#checks if list is sorted or not
sentinel = object()
def is_sorted(a:[int], lo:int = 0, hi:int = sentinel):
    if hi is sentinel:
        hi = len(a)-1
    return all([a[i] <= a[i+1] for i in range(lo, hi)])
