import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will execute first")
    yield
    print("will execute in the last")

@pytest.fixture()
def dataLoad():
    print("user profile details")
    return ["neha", "chorge", "26", "nehachorge.com"]

@pytest.fixture(params=[("Chrome","neha"), ("Firefox", "23", "school"),  "mircosoft Edge"])
def crossBrowser(request):
    return request.param
