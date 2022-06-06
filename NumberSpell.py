class NumberSpell:
    def __init__(self,n):
        self.spell = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        self.n = n
        self.printSpell(self.n)



    def printSpell(self,n):
        if(n==0):
            return
        last_digit = n%10
        self.printSpell(n//10)
        print(self.spell[last_digit])

num = NumberSpell(123456789)