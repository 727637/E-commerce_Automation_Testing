#method name should have some sense bcz at the end this is the test case
# -k --> method name execution
# -s --> logs in output
#-v --> more info like meta data
#can run specific file --> py.test <filename>
#can mark tests(tags) and then run with -m
import pytest


@pytest.mark.smoke
#@pytest.mark.skip

def test_isrtprogram():
    msg = "Hello Neha"
    assert msg == "hi", "test case failed bcz condition do not match"

def test_newtc():
    a = 4
    b = 7
    assert a > 2, "this is not correct"

def test_OpenLayers():
    print("done! it opens with base map")

def test_Openlayers001():
    print("this is second TC")