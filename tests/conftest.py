import pytest
from i2cdevice import MockSMBus


@pytest.fixture(scope='function', autouse=False)
def i2c_dev():
    yield MockSMBus(1)
