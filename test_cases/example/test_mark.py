import os

import pytest


class TestMark():

    def setup_class(self):
        print("setup class")

    # pytest.mark.xfail
    # if condition: jump this test case and mark 'x'
    @pytest.mark.xfail(reason="Testing...", condition=1)
    def test_1(self):
        raise ValueError("TEST....")

    # pytest.mark.skip(reason="")
    # if condition skip
    @pytest.mark.skipif(reason="Test skip", condition=0)
    def test_22(self):
        print(222222)

    # unconditional skip
    @pytest.mark.skip(reason="Test skip")
    def test_33(self):
        print(333333)

    # parametrize， 每次送一个数值
    @pytest.mark.parametrize("foo", [12,6,3,4])
    def test_44(self, foo):
        print(f"test data: {foo}")
        assert foo % 3 == 0


if __name__ == '__main__':
    file = os.path.basename(__file__)
    pytest.main(["-s",file])