"""
# Why fixture?
# if many test cases in one Class, some cases need login, some are not.
# so, add a fixture-login to those who needed.
# other, 1) file or DB open/close
# 2) prepare test data, as parameters to test cases
# 3) login/yield/logout
"""

import pytest
import requests
import os

# Moved to conftest.py
# @pytest.fixture()
# def foo():
#     # this is fixture, it can be used for parameter
#     return "http://www.google.com"
#
#
# @pytest.fixture()
# def bar(foo):
#     # a fixture, use 'foo' fixture
#     resp = requests.get(foo)
#     return resp


@pytest.mark.usefixtures("bar")
def test_web_response(bar):
    # use fixture as parameter
    assert bar.status_code == 200


if __name__ == '__main__':
    file = os.path.basename(__file__)
    pytest.main(['-s', file])


