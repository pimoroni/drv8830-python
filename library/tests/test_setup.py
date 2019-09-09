from i2cdevice import MockSMBus


def test_setup():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    del drv8830
