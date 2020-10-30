from decimal import Decimal

import pytest

from testCalc.calc import Calc

'''
测试方法建议用类包含起来，然后具体测试方法在test_xxx中写
要用到参数化则用@pytest.mark.parametrize
要用到初始化则用setup(每个测试方法都要先做的操作)或setup_class(当前类只做一次的操作)或@pytest.fixture(需要时用调用被fixture修饰的方法名)
'''
class TestCalc:
    def setup_class(self):
        self.calc = Calc()
    def setup(self):
        pass
    @pytest.mark.parametrize('a,b,c',[
        [1,2,2],
        [-1,-1,1],
        [-1,1,-1],
        [-1, 0, 0],
        [1, 0, 0]
    ])
    def test_mul_normal(self,a,b,c):
        assert self.calc.mul(a,b) == c

    @pytest.mark.parametrize('a,b,c', [
        (1.2, 1.5, 1.8),
        (1.25, 2.25, 2.8125),
        (-1.25, -2, 2.5),
        (-1.25, 1.5, -1.875),
        (1.25, 0, 0),
        (-1.25, 0, 0),
    ])
    def test_mul_decimal(self, a, b, c):
        #浮点型数字引入Decimal类将数据转换，然后可以解决浮点计算失精问题，一般在实际代码中控制，不在测试代码中写
        assert self.calc.mul(Decimal(str(a)), Decimal(str(b))) == Decimal(str(c))

    @pytest.mark.parametrize('a,b,c', [
        ['a', 2, 'aa'],
        ['', 2, ''],
        [' ', 0, ''],
        ['@',2,'@@']
    ])
    def test_mul_char(self, a, b,c):
        assert self.calc.mul(a,b) == c

    @pytest.mark.parametrize('a,b,', [
        ['a', '2']
    ])
    def test_mul_exception(self, a, b,):
        #pytest抛出预期异常,可能抛出多个可以用元组
        # with pytest.raises((TypeError,Exception)):
        with pytest.raises(TypeError):
            assert self.calc.mul(a,b)


    @pytest.mark.parametrize('a,b,c',[
        [2,2,1],
        [-1,-1,1],
        [-2,1,-2],
        [0, 1, 0],
        [0, -2, 0]
    ])
    def test_div_normal(self,a,b,c):
        assert self.calc.div(a,b) == c

    @pytest.mark.parametrize('a,b,c',[
        (1, 2, 0.5),
        (2.5, 1, 2.5),
        (-1, -2, 0.5),
        (-25, 5, -5),
        (0, 1.25, 0),
        (0, -1.25, 0),
    ])
    def test_div_decimal(self,a,b,c):
        assert self.calc.div(Decimal(str(a)), Decimal(str(b))) == Decimal(str(c))

    @pytest.mark.parametrize('a,b,c',[
        (1, 3, 0.333333),
        (1, 6, 0.166667),
        (1, -6, -0.166667)
    ])
    def test_div_div(self,a,b,c):
        #通过round方法四舍五入结果,一般不在测试代码中写，在实际代码中控制
        assert round(self.calc.div(Decimal(str(a)), Decimal(str(b))),6) == Decimal(str(c))

    @pytest.mark.parametrize('a,b,', [
        ['a', '2']
    ])
    def test_mul_exception(self, a, b,):
        #pytest抛出预期异常,可能抛出多个可以用元组
        # with pytest.raises((TypeError,Exception)):
        with pytest.raises(TypeError):
            assert self.calc.div(a,b)