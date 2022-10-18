import pytest
import numpy as np
from simple_functions import my_sum, factorial, my_sin


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (2, 2),
        (4, 24)
    ])
    def test_my_fac(self, number, expected):
        '''Test our add function'''
        isum = factorial(number)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (np.pi, 0)])
    def test_my_sin(self, number, expected):
        '''Test our add function'''
        isum = my_sin(number)
        assert isum == expected
