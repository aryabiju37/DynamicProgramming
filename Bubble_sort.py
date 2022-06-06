import numpy as np
class BubbleSort:
    def __init__(self,arr,n):
        self.arr = arr
        self.n = n
        self.j = 0
        #print(self.bubble_sort(self.arr,self.n))
        #print(self.bubble_sort1(self.arr,self.n))
        print(self.bubble_sort2(self.arr,self.n,self.j))

    def comparison(self,a,b):
        return a > b

##without recursion

    def bubble_sort(self,arr,n):
        for i in range(n):
            for j in range(n):
                if(self.comparison(arr[i],arr[j])):
                    arr[i],arr[j] = arr[j],arr[i]
        return arr

## with recursion
    def bubble_sort1(self,arr,n):
        if(n==1):
            return
        for j in range(0,n-1): #inner loop of the previous method is coserved , the outer loop is being
                               #recursively called
            if self.comparison(arr[j],arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
        self.bubble_sort1(arr,n-1)
        return arr

## with recursion inner and outer loop:
    def bubble_sort2(self,arr,n,j):
        if(n==1):
            return
        if(j==n-1):
            self.bubble_sort2(arr,n-1,0)
            return
        if(self.comparison(arr[j],arr[j+1])):
            arr[j],arr[j+1] = arr[j+1],arr[j] #line 41,42 and 43 are the modified inner loops
        self.bubble_sort2(arr,n,j+1)
        return arr





arr = np.array([-12,4,1,7,5,-1])
n = arr.shape[0]
Bub = BubbleSort(arr,n)



