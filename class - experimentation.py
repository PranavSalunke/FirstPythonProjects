import random

class numbers():
        def __init__(self,n):
                self.num1 = random.randint(1,n)
                self.num2 = random.randint(1,n)
        def addnum(self):
                self.add = self.num1 + self.num2
                return self.add
        def multnum(self):
                self.mult = self.num1 * self.num2
                return self.mult
        def divnum(self):
                '''
                divide num1 by num2
                '''
                self.div = self.num1/self.num2
                return self.div 
