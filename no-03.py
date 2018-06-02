import time
import random

class Sort:
    limit = 5
    count = 0

    def __init__(self, data = None):
        if data == None:
            self.data = []
        else:
            self.data = data

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

    def combosort(self):
        self.quick_insert(0, len(self.data) - 1)

def binary(target, arr, start, end):
    if start <= end:
        middle = int((start + end) / 2)
        if target == arr[middle]:
            return middle + 1
        elif target < arr[middle]:
            return binary(target, arr, start, middle-1)
        else:
            return binary(target, arr, middle+1, end)
    else:
        return -1

def binary_search(target, arr):
    return binary(target, arr, 0, len(arr))

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

sorter = Sort(a)
sorter.combosort()

a = sorter.data
print (a)

print (binary_search(4, a))
