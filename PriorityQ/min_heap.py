class MinHeap:
    def __init__(self, arr=[]):
        self.arr = arr
        n = len(self.arr)

        if not n == 0:
            for i in range(n // 2, -1, -1):
                self.min_heapify(i)

    def insert(self, x):
        # where x will go
        i = len(self.arr)
        # actual insert
        self.arr.append(x)
        # keep invariant
        self.swim(i)

    def min_heapify(self, parent):
        # if no left child return
        if not 2 * parent + 1 < len(self.arr):
            return

        # if no right child
        if not 2 * parent + 2 < len(self.arr):
            smaller = 2 * parent + 1

        # get index of smaller child
        elif self.arr[2 * parent + 1] < self.arr[2 * parent + 2]:
            smaller = 2 * parent + 1
        else:
            smaller = 2 * parent + 2

        # if smaller than parent, swap
        if self.arr[smaller] < self.arr[parent]:
            self.arr[parent], self.arr[smaller] = self.arr[smaller], self.arr[parent]
            self.min_heapify(smaller)

    def min(self):
        return self.arr[0]

    def delete_min(self):
        # swap min with last element
        min = self.arr[0]
        i = len(self.arr) - 1
        self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
        # remove min from array
        self.arr.pop()

        # fix invariant
        self.min_heapify(0)
        return min

    def swim(self, x):
        # go up while invariant is violated
        while x > 0:
            if not self.arr[x] < self.arr[(x - 1) // 2]:
                break
            self.arr[(x - 1) // 2], self.arr[x] = self.arr[x], self.arr[(x - 1) // 2]
            x = (x - 1) // 2


# h = MinHeap([532, 234, 324, 23, 0, 3, 6, 23, 4, 6, 89, 20])
#
# print(h.arr)
#
# n = 100
# arr = random.sample(range(-523000, 14252000), n)
#
# h2 = MinHeap(arr)
# assert
# print(h2.arr)
