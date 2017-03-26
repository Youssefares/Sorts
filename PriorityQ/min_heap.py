
class MinHeap:

    def __init__(self, arr = []):
        self.arr = arr
        n = len(self.arr)

        if not n == 0:
            for i in range(n//2):
                self.min_heapify(i)


    def insert(self, x):
        #where x will go
        i = len(self.arr)
        #actual insert
        self.arr.append(x)
        #keep invariant
        self.swim(i)


    def min_heapify(self, parent):
        arr = self.arr
        #if no left child return
        if not 2*parent+1 < len(arr):
            return

        #if no right child
        if not 2*parent+2 < len(arr):
            smaller = 2*parent+2

        #get index of smaller child
        elif arr[2*parent +1] < arr[2*parent +2]:
            smaller = 2*parent+1
        else:
            smaller = 2*parent+2

        #if smaller than parent, swap
        if arr[smaller] < arr[parent]:
            arr[parent], arr[smaller] = arr[smaller], arr[parent]
            self.min_heapify(smaller)


    def min(self):
        return self.arr[0]

    def delete_min(self):
        arr = self.arr
        #swap min with last element
        min = arr[0]
        i = len(self.arr) -1
        arr[0], arr[i] = arr[i], arr[0]
        #remove min from array
        arr.pop()

        #fix invariant
        self.min_heapify(0)
        return min


    def swim(self, x):
        arr = self.arr
        #go up while invariant is violated
        while not x == 0:
            if not arr[x] < arr[(x-1)//2]:
                break
            arr[(x-1)//2], arr[x] = arr[x], arr[(x-1)//2]
            x = (x-1)//2
