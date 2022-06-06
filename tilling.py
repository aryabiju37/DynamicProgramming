class Tilling:
    def __init__(self,n,m):
        self.n = n
        self.m = m
        print(self.till(self.n,self.m))

    def till(self,n,m):
        ##base case
        if(n<=m-1):
            return 1

        return self.till(n-1,m) + self.till(n-m,m)

tilli = Tilling(7,4)
