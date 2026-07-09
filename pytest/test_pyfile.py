#filename start or end with test_ or _test
#assert function should start with test_

string="python"
def convertstring(string):
    return string.upper()
def test_convertstring():
    assert convertstring(string)=="PYTHON"