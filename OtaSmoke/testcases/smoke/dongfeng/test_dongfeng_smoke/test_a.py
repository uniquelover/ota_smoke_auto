import pytest


def test_a(): 
    print("------->test_a")
    assert 1 
def test_b():
    print("------->test_b")
    assert 0 


if __name__ == '__main__':
    pytest.main(["-s","test_abc.py"]) 
