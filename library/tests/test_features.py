from i2cdevice import MockSMBus


def test_forward():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    drv8830.forward()


def test_reverse():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    drv8830.reverse()


def test_brake():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    drv8830.brake()


def test_coast():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    drv8830.coast()
