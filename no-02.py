class Quicksort:
    def __init__(self, Data, Limit = 0):
        self.data = Data
        self.amount = len(self.data) - 1
        self.indeks = 0
        self.limit = Limit
        
    def partition(self, start, end):
        pivot = start

        for i in range(start, end):
            if self.data[i] < self.data[end]:
                self.data[i], self.data[pivot] = self.data[pivot], self.data[i]
                pivot += 1
        
        self.data[pivot], self.data[end] = self.data[end], self.data[pivot]

        return pivot

    def insert(self, start, end):
        if start<end:
            if (self.data[end] < self.data[end-1]):
                self.data[end], self.data[end-1] = self.data[end-1], self.data[end]
                self.insert(start, end-1)

    def insertion(self, start, end):
        if self.indeks <= (end - start):
            self.insert(start , self.indeks + start)
            self.indeks += 1
            self.insertion(start, end)

    def quicksort(self, start, end):
        if start < end:
            pivot = self.partition(start, end)

            if (pivot-1 - start) < self.limit:
                print ("Insert 1")
                self.insertion(start, pivot-1)
            else:
                print ("Quick 2")
                self.quicksort(start, pivot-1)

            if (end - pivot+1) < self.limit:
                print ("Insert 2")
                self.insertion(pivot+1, end)
            else:
                print ("Quick 2")
                self.quicksort(pivot+1, end)

    def user_quick_out(self):
        self.quicksort(0, self.amount)
        print (self.data)

data = [19,62,0,97,4,5,88,3,41,55,74,234,75,23,94,53,24,8,5,4]
quick = Quicksort(data, 10)

quick.user_quick_out()
