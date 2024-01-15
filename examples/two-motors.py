import time

from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR2

left = DRV8830(I2C_ADDR1)
right = DRV8830(I2C_ADDR2)

# Give the motors some voltage (speed)
left.set_voltage(5)
right.set_voltage(5)

# Move forward
left.forward()
right.forward()
time.sleep(1.0)

# Turn left
left.reverse()
right.forward()
time.sleep(1.0)

# Turn right
left.forward()
right.reverse()
time.sleep(1.0)

# Move backward
left.reverse()
right.reverse()
time.sleep(1.0)

# Coast to a stop
left.coast()
right.coast()
time.sleep(1.0)

# Reduce voltages to zero
left.set_voltage(0)
right.set_voltage(0)
