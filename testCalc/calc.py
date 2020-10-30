
#定义一个计算类，里面有乘法和除法
from decimal import Decimal


class Calc:
    #在方法名上右击，点击generate-Test...，可以快速生成该方法的测试方法
    def div(self,a,b):
        return a/b
    def mul(self,a,b):
        return a*b

# calc=Calc()
# print(calc.div((1,2), 0))
# print(calc.mul(Decimal('1.2'), Decimal('1.5')))