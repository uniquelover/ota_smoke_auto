#!/usr/bin/env python3

"""
@ name: test_one.py
@ date: 12/7/2020
"""


import pytest


def test_a():

    print('test_a function----')
    assert 1

# def test_b():
#     print('test_b functions----')
#     assert 0


def test_c():
    print("test_c function----")


def test_d(log_in):
    print('test_d function----')


if __name__ == "__main__":
    pytest.main(["test_one.py", "-s"])
