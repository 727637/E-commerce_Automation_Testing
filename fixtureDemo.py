import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo1(self):
        print("i will execute later 1")

    def test_fixtureDemo2(self):
        print("i will execute later 2")

    def test_fixtureDemo3(self):
        print("i will execute later 3")