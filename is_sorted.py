#checks if list is sorted or not
sentinel = object()
def is_sorted(a:[int], lo:int = 0, hi:int = sentinel):
    if hi is sentinel:
        hi = len(a)-1
    return all([a[i] <= a[i+1] for i in range(lo, hi)])


#testing
assert is_sorted([2,3,3,5])
assert is_sorted([1])
assert not is_sorted([2,0])
assert is_sorted([2,3,4,5,0,234,0], 0, 3)
assert not is_sorted([2,3,4,5,234,0], 4, 5)
assert is_sorted([53,2,0], 2, 2)
