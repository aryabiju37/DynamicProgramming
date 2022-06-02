'''
Understanding recursion directions :
print asc and desc:
Base Case : if N==0 : return 1


'''
import numpy as np

class Prnt:
    def __init__(self,n):
        self.n=n
        self.desc(self.n)
        self.inc(self.n)

    def desc(self,n):
        if (n==0):
            return
        print(n)
        self.desc(n-1)

    def inc(self,n):
        if(n==0):
            return
        self.inc(n-1)
        print(n)

printnum = Prnt(5)

class FirstOccur:
    def __init__(self,arr,n,key):
        self.arr = arr
        self.n = n
        self.key = key
        self.lst = []

        print(self.first_occur(self.arr,self.n,self.key))
        print(self.last_occurence(self.arr,self.n,self.key))
        print(self.find_all_occurences(self.arr,self.n,self.key))


    def first_occur(self,arr,n,key):
        ##base case
        if n==0:
            return -1
        ## recursion case
        if(arr[0]==key):
            return 0
        occurences = self.first_occur(arr[1:],n-1,key)
        if occurences != -1:
            return occurences+1
        return -1

    def last_occurence(self,arr,n,key):
        ##base case:
        if n==0:
            return -1
        ##recursive case
        sub_index = self.last_occurence(arr[1:],n-1,key)
        if (sub_index == -1):
            if arr[0]== key:
                return 0
            else:
                return -1
        else:
            return sub_index+1

    def find_all_occurences(self,arr,n,key):
        # base case:
        if n==0:
            return []
        #recursive case:
        sub_index = self.find_all_occurences(arr[1:],n-1,key)
        if sub_index == [] and self.lst ==[]:
            if(arr[0]==key):
                self.lst.append(self.n-n)
                return self.lst
            else:
                return []
        elif sub_index != []:
            if(arr[0] == key):
                self.lst.append(self.n-n)
                return self.lst
            else:
                return list(reversed(self.lst))











arr = np.array([1,2,3,1,2,3,1,2,3,1,2,3,7,3,7,8,7,6,7])
n = arr.shape[0]
key = 7
frst=FirstOccur(arr,n,key)


