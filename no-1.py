class Quicksort:
    def __init__(self, Data):
        self.data = Data
        self.amount = len(self.data) - 1
        
    def partition(self, start, end):
        pivot = start

        for i in range(start, end):
            if self.data[i] < self.data[end]:
                self.data[i], self.data[pivot] = self.data[pivot], self.data[i]
                pivot += 1
        
        self.data[pivot], self.data[end] = self.data[end], self.data[pivot]

        return pivot

    def quicksort(self, start, end):
        if start < end:
            pivot = self.partition(start, end)
            self.quicksort(start, pivot-1)
            self.quicksort(pivot+1, end)
    
    def user_quick_out(self):
        self.quicksort(0, self.amount)
        print (self.data)

data = [19,62,0,97,44,8,99,25,74,68,56,62,84,4,70,74,6,33,82,7,9]
quick = Quicksort(data)

quick.user_quick_out()
