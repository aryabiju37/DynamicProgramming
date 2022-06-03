''' print increasing number
input 5
output 1,2,3,4,5
'''
class Rec:
    def __init__(self,n):
        self.n = n
        self.printNumbers(self.n)

    def printNumbers(self,n):
        if n==0:
            return
        self.printNumbers(n - 1)
        print(n)


rec = Rec(5)

'''
fast power calculation
'''
class Power:
    def __init__(self,a,n):
        self.a = a
        self.n = n
        print(self.fast_power(self.a,self.n))

    def fast_power(self,a,n):
        if (n==0):
            return 1
        else:
            sub_problem = self.fast_power(a,n//2)
            sub_sq = sub_problem * sub_problem
            if (n%2 != 0):
                return a*sub_sq
            else:
                return sub_sq

pow = Power(2,5)



