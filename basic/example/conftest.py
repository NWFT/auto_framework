"""
# Why conftest.py
# if one Fixture, want to be used for many test-files.
# put Fixture in conftest.py, all files need NOT write again.
# the name is fixed, and only can be used in the same dir
# fixture(scope="function" / session>module>class>function)
# function: - every function/method will be used
# class:    - every class(mark.usefixtures), used once
# module:   - every .py, used once
# session:  - one project, used once
"""
import pytest
import requests


@pytest.fixture()
def foo():
    # this is fixture, it can be used for parameter
    return "http://www.google.com"


@pytest.fixture()
def bar(foo):
    # a fixture, use 'foo' fixture
    resp = requests.get(foo)
    return resp


@pytest.fixture(scope='class')
def class_fixture():
    print("Class fixture, before yield")
    yield
    print("Class fixture, after yield")


@pytest.fixture(scope='module')
def module_fixture():
    print("Module fixture, before yield")
    yield
    print("Module fixture, after yield")


@pytest.fixture(scope='session')
def session_fixture():
    print("Session fixture, before yield")
    yield
    print("Session fixture, after yield")







