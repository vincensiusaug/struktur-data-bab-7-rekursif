import time
import random

class Sort:
    def __init__(self, amount):
        self.count = 0
        self.data = []
        self.data_assign(amount)
    
    def data_assign(self, amount):
        if amount > 0:
            self.data_assign(amount-1)
        self.data.append(random.randint(1, 99))

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

    def efective_time(self):
        return ("{0:.4}".format(self.waktu*1000))

    def efective_count(self):
        return self.count

jumlah = int(input("Masukan jumlah data = "))

quick = []
total = 0

for i in range(10):
    quick.append(Sort(jumlah))
    quick[i].quicksort()
    total += float(quick[i].efective_time())

total = total/jumlah
print ("Waktu rata-rata dari {0:} data adalah {1:.4}ms".format(jumlah, total))
