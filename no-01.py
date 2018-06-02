import time

class Sort:
    def __init__(self, data):
        self.data = data
        self.count = 0

    def partition(self, start, end):
        pivot = start

        def comparator(i, end, pivot):
            if i < end:
                self.count += 1
                if self.data[i] < self.data[end]:
                    self.data[i], self.data[pivot] = self.data[pivot], self.data[i]
                    pivot += 1
                pivot = comparator(i+1, end, pivot)
            return pivot

        pivot = comparator(start, end, pivot)

        # for i in range(start, end):
        #     if self.data[i] < self.data[end]:
        #         self.data[i], self.data[pivot] = self.data[pivot], self.data[i]
        #         pivot += 1
        
        self.data[pivot], self.data[end] = self.data[end], self.data[pivot]

        return pivot

    def quick(self, start, end):
        if start < end:
            pivot = self.partition(start, end)
            self.quick(start, pivot-1)
            self.quick(pivot+1, end)

    def quicksort(self):
        self.waktu = time.time()
        self.quick(0, len(self.data) - 1)
        self.waktu = time.time() - self.waktu
        return self.data

    def efective_time(self):
        return ("%16.6f"%(self.waktu))

    def efective_count(self):
        return self.count

a = [1,3,9,10,44,4,5,7,89,14,10]

b = Sort(a)


print (a, b.quicksort(), b.efective_time(), b.efective_count())
