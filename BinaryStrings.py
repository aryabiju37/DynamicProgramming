"""input 3 : output:000,001,010,011,100,101,110,111"""
import numpy as np
class BinaryStrings:
    def __init__(self,n):
        self.n = n
        self.a = []*2**n
        print(self.binstr(self.n,self.a))

    def binstr(self,n,arr):
        ##all possible values according to n
        str = "-1"*n
        for i in range(len(arr)):
            for j in range(n):
                str[j] = "0"*n
            arr.append(str)
        return arr
bin = BinaryStrings(3)


