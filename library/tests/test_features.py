def test_forward(i2c_dev):
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    drv8830.forward()


def test_reverse(i2c_dev):
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    drv8830.reverse()


def test_brake(i2c_dev):
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    drv8830.brake()


def test_coast(i2c_dev):
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    drv8830.coast()


def test_set_outputs(i2c_dev):
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    drv8830.set_outputs(out1=0, out2=0)


def test_set_voltage(i2c_dev):
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    drv8830.set_voltage(5.06)
    assert drv8830.get_voltage() == 5.06


def test_set_voltage_snap(i2c_dev):
    # Should snap to the nearest available voltage and read back correctly
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    drv8830.set_voltage(0.82)
    assert drv8830.get_voltage() == 0.80


def test_voltage_out_of_range(i2c_dev):
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    drv8830.set_voltage(0)
    assert drv8830.get_voltage() == 0


def test_get_fault(i2c_dev):
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    assert drv8830.get_fault().current_limit == 0


def test_clear_fault(i2c_dev):
    from drv8830 import DRV8830
    drv8830 = DRV8830(i2c_dev=i2c_dev)
    drv8830.clear_fault()
