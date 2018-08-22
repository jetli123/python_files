class MuffedCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else:
                raise

calculator = MuffedCalculator()
#print calculator.calc('10/2')
#print calculator.calc('4/0')

calculator.muffled = True
print calculator.calc('10/0')