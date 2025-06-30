#any python file should start with test_ or end with _test
#pytest method (def ) should always start with test_ or can end with _test
#CODE SHOULD BE WRAPPED IN METHOD
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("hello, welcome to pytest")

#@pytest.mark.xfail
def test_secondTestcase():
    print("it is going well")


@pytest.mark.smoke
def test_thirdTestCAse():
    print("secont attempt")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
