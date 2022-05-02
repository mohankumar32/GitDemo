import pytest

from pythonSelfFramework.tests.utilities import BaseClass

@pytest.mark.usefixtures

class e2eTestClass(BaseClass):

    def e2eTestCase(self, setup):
        setup.dri
