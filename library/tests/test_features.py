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


def test_set_outputs():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    drv8830.set_outputs(out1=0, out2=0)


def test_set_voltage():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    drv8830.set_voltage(5.06)
    assert drv8830.get_voltage() == 5.06


def test_set_voltage_snap():
    # Should snap to the nearest available voltage and read back correctly
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    drv8830.set_voltage(0.82)
    assert drv8830.get_voltage() == 0.80


def test_voltage_out_of_range():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    drv8830.set_voltage(0)
    assert drv8830.get_voltage() == 0


def test_get_fault():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    assert drv8830.get_fault().current_limit == 0


def test_clear_fault():
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=MockSMBus(1))
    drv8830.clear_fault()
