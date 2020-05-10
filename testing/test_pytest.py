import pytest
import yaml

from python.calc import Calc


class TestCal():
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('a,b', yaml.safe_load(open("./data.yaml")))
    def test_add_1(self, a, b):
        # self.calc = Calc()

        result = self.calc.add(a, b)

        print(result)

        # assert 3 == result

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open("./data.yaml")))

    def test_div_2(self, a, b):
        # self.calc = Calc()
        result1 = self.calc.div(a, b)
        print(result1)

# if __name__ == '__main__':
#     pytest.main(['-vs', 'test_pytest.py::TestCal::test_div_2'])
