import pytest


def get_divid(x):
    if x == 0:
        raise ValueError("parameter not zero")
    return 10/x


class TestCases:
    def setup(self):
        print("setup in class")

    def teardown(self):
        print("teardown in class")

    def setup_class(self):
        print("Class-setup")

    def teardown_class(self):
        print("Class-teardown")

    def test_01(self):
        # test 0
        with pytest.raises(Exception, match="parameter not zero") as except_obj:
            result = get_divid(0)
        assert except_obj.type == ValueError

    def test_02(self):
        result = get_divid(1)
        assert result == 10


def test_abc():
    assert "abc" == "abc"

def setup_module():
    # The whole project
    print("Module-setup")

def teardown_module():
    # if error, not execute
    print("Module-teardown")

def setup_function():
    # only test* function, no methods
    print("Function-setup")

def teardown_function():
    print("Function-teardown")


if __name__ == '__main__':
    pytest.main(["-s"])