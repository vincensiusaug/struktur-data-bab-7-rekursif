import time
import random

class Sort:
    limit = 5
    count = 0

    def __init__(self, data = None):
        if data == None:
            self.data = []

    def data_assign(self, amount):
        for i in range(amount):
            self.data.append(random.randint(1, 99))

    def partition(self, start, end):
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

    def insert(self, start, end, indeks = None, rec = 0):
        if indeks == None:
            indeks = start + 1

        if indeks >= start and indeks <= end:
            data = self.data
            self.count += 1
            if rec == 0:
                self.fr = indeks

            if data[self.fr] < data[indeks-1] and indeks != 0:
                self.insert(start, end, indeks-1, rec+1)

            elif rec != 0:
                data.insert(indeks, data.pop(self.fr))

            if rec == 0:
                self.insert(start, end, indeks+1)

    def quick(self, start, end):
        if start < end:
            pivot = start + self.partition(start, end)
            self.quick(start, pivot-1)
            self.quick(pivot+1, end)
    
    def quick_insert(self, start, end):
        if start < end:
            pivot = start + self.partition(start, end)
            if (pivot - 1) - start < self.limit:
                self.insert(start, pivot - 1)
            else:
                self.quick_insert(start, pivot - 1)
                
            if end - (pivot + 1) < self.limit:
                self.insert(pivot + 1, end)
            else:
                self.quick_insert(pivot + 1, end)

    def quicksort(self):
        self.waktu = time.time()
        self.quick(0, len(self.data) - 1)
        self.waktu = time.time() - self.waktu

    def insertsort(self):
        self.waktu = float(time.time())
        self.insert(0, len(self.data) - 1)
        self.waktu = time.time() - self.waktu

    def combosort(self):
        self.waktu = time.time()
        self.quick_insert(0, len(self.data) - 1)
        self.waktu = time.time() - self.waktu

    def test(self, choice):
        if choice == "quick":
            self.quicksort()
        elif choice == "insert":
            self.insertsort()
        else:
            self.combosort()

def compare_sort():
    data_total = int(input("Masukan jumlah data = "))
    combo_limit = int(input("Masukan limit untuk combo sort = "))
    class_total = 1000

    for mode in ("quick", "insert", "combo"):
        sorter = []
        time_total = 0
        step_total = 0
        
        for i in range(class_total):
            sorter.append(Sort())

            sorter[i].data_assign(data_total)

            sorter[i].limit = combo_limit
            sorter[i].test(mode)

            time_total += sorter[i].waktu
            step_total += sorter[i].count

        time_total = time_total/class_total
        step_total = step_total/class_total

        print ("\nMode {0:}sort\nWaktu =  {1:.6f} detik\nLangkah =  {2:.0f}".format(mode, time_total, step_total))

compare_sort()
