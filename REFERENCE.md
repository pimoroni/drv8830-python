# Reference <!-- omit in toc -->

- [Getting Started](#getting-started)
  - [Installing](#installing)
- [Examples](#examples)
  - [Two Motors](#two-motors)
- [Function Reference](#function-reference)
  - [set_voltage](#set_voltage)
  - [get_voltage](#get_voltage)
  - [set_outputs](#set_outputs)
  - [brake](#brake)
  - [coast](#coast)
  - [forward](#forward)
  - [reverse](#reverse)
  - [set_direction](#set_direction)
  - [get_fault](#get_fault)
  - [clear_fault](#get_fault)


## Getting Started

Most people should grab the library from GitHub and run our simple installer:

### Installing

```
git clone https://github.com/pimoroni/drv8830-python
cd drv8830-python
sudo ./install.sh
```

This ensures any dependencies are installed and will copy examples into `~/Pimoroni/drv8830/`

You can install just the drv8830 library by running:

```
sudo pip3 install drv8830
```

## Examples

### Two Motors
[two-motors.py](examples/two-motors.py)

Demonstrates the use of two DRV8830 drivers as part of a two-wheeled robot.


## Function Reference

In all cases you'll first need to initialise a DRV8830 library instance with the specific I2C address for each driver you're using.

```python
from drv8830 import DRV8830, I2C_ADDR1

drv8830 = DRV8830(i2c_addr=I2C_ADDR1)
```

The value that you use for `i2c_addr` will vary depending on your I2C address jumper configuration:

* `I2C_ADDR1` - `0x60` - both select jumpers bridged (not cut) (default)
* `I2C_ADDR2` - `0x61` - only jumper A0 cut (ADDR+1)
* `I2C_ADDR3` - `0x63` - only jumper A1 cut (ADDR+3)
* `I2C_ADDR4` - `0x64` - both A0 and A1 cut (ADDR+1 and ADDR+3)

Ensure care when cutting jumpers, use the point of a sharp hobby-knife and avoid slipping since this may damage other traces.

### set_voltage

```python
drv8830.set_voltage(voltage)
```

Set the motor driver voltage.

Roughly corresponds to motor speed depending upon the characteristics of your motor.

Value values range from 0.48v to 5.06v

### get_voltage

```python
voltage = drv8830.get_voltage()
```

Returns the currently set voltage value from the DRV8830.

### set_outputs

```python
drv8830.set_outputs(out1, out2)
```

Set the individual driver outputs. Eg:

```python
drv8830.set_outputs(1, 0)
```

Possible values are 1 (on) and 0 (off) with the following valid permutations:

* 1 1 - brake
* 0 0 - coast
* 1 0 - forward
* 0 1 - reverse

### brake

```python
drv8830.brake()
```

Drives both outputs high, effectively braking the motor.

Does the same as `drv8830.set_outputs(1, 1)` or `drv8830.set_direction("brake")`.

### coast

```python
drv8830.coast()
```

Drives both outputs low, allowing the motor to coast to a stop.

Does the same as `drv8830.set_outputs(0, 0)` or `drv8830.set_direction("coast")`.

### forward

```python
drv8830.forward()
```

Drives one output high and the other low, effectively turning the motor "forwards" (albeit this depends on how your motor is positioned and wired)

Does the same as `drv8830.set_outputs(1, 0)` or `drv8830.set_direction("forward")`.

### reverse

```python
drv8830.forward()
```

Drives one output high and the other low, effectively turning the motor in "reverse" (albeit this depends on how your motor is positioned and wired)

Does the same as `drv8830.set_outputs(0, 1)` or `drv8830.set_direction("reverse")`.

### set_direction

```python
drv8830.set_direction(direction)
```

Accepts a string and sets the direction to the supplied "forward", "backward", "brake" or "coast".

### get_fault

```python
fault = drv8830.get_fault()
```

Returns a namedtuple of the fault flags:

* `current_limit` - external current limit exceeded (ilimit resistor), must clear fault or disable motor to reactivate
* `over_temperature` - driver has overheated, device resumes once temperature has dropped
* `under_voltage` - driver is below operating voltage (brownout), resumes once voltage has stabalised
* `over_current` - over-current protection activated, device disabled, must clear fault to reactivate
* `fault` - one or more fault flags is set

### clear_fault

```python
drv8830.clear_fault()
```

Clear any outstanding fault conditions.
