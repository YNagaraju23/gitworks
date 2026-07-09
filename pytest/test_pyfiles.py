# content of test_sample.py
def fun(x):
    return x + 1
def test_answer():
    assert fun(4) == 5

def fun(a):
    return a+20
def test_answer():
    assert fun(10) == 30