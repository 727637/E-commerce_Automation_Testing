import pytest

from pyTestDemo.baseClass import BaseClass
from pyTestDemo.conftest import dataLoad


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        #print(dataLoad[0])

        #print(dataLoad[2])