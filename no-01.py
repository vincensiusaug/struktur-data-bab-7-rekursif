import time
import random

class Sort:
    count = 0

    def __init__(self, model, data = None):
        self.model = model
        if data == None:
            self.data = []
    
    def data_assign(self, amount):
        if amount > 1:
            self.data_assign(amount-1)
        self.data.append(random.randint(1, 99))

    def partition1(self, start, end):
        data = self.data[start:end+1]

        pivot = int(len(data)/2)

        pivot_num = data[pivot]
        data_1 = data[:pivot]
        data_2 = data[pivot+1:]
    
        def comparator_1(indeks = 0):
            if indeks < len(data_1):
                self.count += 1
                if data_1[indeks] > pivot_num:
                    data_2.append(data_1.pop(indeks))
                    comparator_1(indeks)
                else:
                    comparator_1(indeks+1)
        
        def comparator_2(indeks = 0):
            if indeks < len(data_2):
                self.count += 1
                if data_2[indeks] < pivot_num:
                    data_1.append(data_2.pop(indeks))
                    comparator_2(indeks)
                else:
                    comparator_2(indeks+1)

        comparator_1()
        comparator_2()

        pivot = len(data_1)
        data_1.append(pivot_num)
        data = data_1 + data_2

        self.data[start:end+1] = data
        return pivot

    def partition2(self, start, end):
        data = self.data[start:end+1]

        pivot = 0
        
        pivot_num = data[pivot]
        data_1 = data[:pivot]
        data_2 = data[pivot+1:]
    
        def comparator_1(indeks = 0):
            if indeks < len(data_1):
                self.count += 1
                if data_1[indeks] > pivot_num:
                    data_2.append(data_1.pop(indeks))
                    comparator_1(indeks)
                else:
                    comparator_1(indeks+1)
        
        def comparator_2(indeks = 0):
            if indeks < len(data_2):
                self.count += 1
                if data_2[indeks] < pivot_num:
                    data_1.append(data_2.pop(indeks))
                    comparator_2(indeks)
                else:
                    comparator_2(indeks+1)

        comparator_1()
        comparator_2()

        pivot = len(data_1)
        data_1.append(pivot_num)
        data = data_1 + data_2

        self.data[start:end+1] = data
        return pivot

    def partition3(self, start, end):
        data = self.data[start:end+1]

        pivot = len(data)-1
        
        pivot_num = data[pivot]
        data_1 = data[:pivot]
        data_2 = data[pivot+1:]
    
        def comparator_1(indeks = 0):
            if indeks < len(data_1):
                self.count += 1
                if data_1[indeks] > pivot_num:
                    data_2.append(data_1.pop(indeks))
                    comparator_1(indeks)
                else:
                    comparator_1(indeks+1)
        
        def comparator_2(indeks = 0):
            if indeks < len(data_2):
                self.count += 1
                if data_2[indeks] < pivot_num:
                    data_1.append(data_2.pop(indeks))
                    comparator_2(indeks)
                else:
                    comparator_2(indeks+1)

        comparator_1()
        comparator_2()

        pivot = len(data_1)
        data_1.append(pivot_num)
        data = data_1 + data_2

        self.data[start:end+1] = data
        return pivot

    def quick(self, start, end):
        if start < end:
            if self.model == 1:
                pivot = start + self.partition1(start, end)
            elif self.model == 2:
                pivot = start + self.partition2(start, end)
            else:
                pivot = start + self.partition3(start, end)
            self.quick(start, pivot-1)
            self.quick(pivot+1, end)

    def quicksort(self):
        self.waktu = time.clock()
        self.quick(0, len(self.data) - 1)
        self.waktu = time.clock() - self.waktu


data_total = int(input("Masukan jumlah data = "))
class_total = 1000

for model in range(1, 4):
    quick = []
    time_total = 0
    step_total = 0
    for i in range(class_total):
        quick.append(Sort(model))

        quick[i].data_assign(data_total)
        quick[i].quicksort()

        time_total += quick[i].waktu
        step_total += quick[i].count

    time_total = time_total/class_total
    step_total = step_total/class_total

    print ("\nModel {0:}\nWaktu =  {1:.6f} detik\nLangkah =  {2:.0f}".format(model, time_total, step_total))
