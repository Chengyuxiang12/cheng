import pytest
import yaml
import sys

sys.path.append("..")
from python.calc import Calc
from decimal import Decimal


class TestCal():
    @pytest.fixture()
    def setup(self):
        self.calc = Calc()

    @pytest.mark.add
    @pytest.mark.parametrize('a,b', yaml.safe_load(open("../python/data.yaml")))
    def calc_add_1(self, a, b,setup):
        result1 = self.calc.add(a, b)
        c = a + b
        assert result1 == c
        print(result1)

    @pytest.mark.parametrize('a,b', yaml.safe_load(open("../python/data.yaml")))
    @pytest.mark.div
    def calc_div_1(self, a, b,setup):
        try:
            result1 = self.calc.div(a, b)

        except:
            return 'division by zero'
            assert result1 == 'division by zero'
        assert result1 == a / b

        print(result1)

    @pytest.mark.parametrize('a,b', yaml.safe_load(open("../python/data.yaml")))
    @pytest.mark.mul
    def calc_multiply_1(self, a, b,setup):
        result1 = self.calc.multiply(a, b)
        assert result1 == a * b
        print(result1)

    @pytest.mark.parametrize('a,b', yaml.safe_load(open("../python/data.yaml")))
    @pytest.mark.sub
    def calc_subtract_1(self, a, b,setup):
        result1 = self.calc.subtract(a, b)
        assert result1 == a - b
        print(result1)
