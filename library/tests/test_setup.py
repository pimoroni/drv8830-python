from i2cdevice import MockSMBus


def test_setup():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    del drv8830


def test_setup_alt_addr2():
    from drv8830 import DRV8830, I2C_ADDR2
    drv8830 = DRV8830(i2c_dev=MockSMBus(1), i2c_addr=I2C_ADDR2)
    del drv8830


def test_setup_alt_addr3():
    from drv8830 import DRV8830, I2C_ADDR3
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    drv8830.select_i2c_address(I2C_ADDR3)
