def test_setup(i2c_dev):
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    del drv8830


def test_setup_alt_addr2(i2c_dev):
    from drv8830 import DRV8830, I2C_ADDR2
    drv8830 = DRV8830(i2c_dev=i2c_dev, i2c_addr=I2C_ADDR2)
    del drv8830


def test_setup_alt_addr3(i2c_dev):
    from drv8830 import DRV8830, I2C_ADDR3
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    drv8830.select_i2c_address(I2C_ADDR3)
