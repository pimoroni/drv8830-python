from i2cdevice import Device, Register, BitField
from i2cdevice.adapter import Adapter, LookupAdapter


__version__ = '0.0.1'


class VoltageAdapter(Adapter):
    # Calculation is ostensibly 4 * 1.285V (vref) * (vset + 1) / 64
    # But appears closer to round(4 * 1.285 * i / 64.0 + 0.0001, 2)
    # Then the datasheet goes on to detail individual voltages that
    # neither of these formulae round consistently to.
    # So we'll take some liberties with them instead.
    def _decode(self, i):  # index to voltage
        if i <= 5:
            return 0
        offset = 0.01 if i >= 16 else 0
        offset += 0.01 if i >= 48 else 0
        return round(offset + i * 0.08, 2)

    def _encode(self, v):  # voltage to index
        if v < 0.48:
            return 0
        offset = -0.01 if v >= 1.29 else 0
        offset -= 0.01 if v >= 3.86 else 0
        return int(offset + v / 0.08)


class DRV8830:
    def __init__(self, i2c_addr=None, i2c_dev=None):
        self._i2c_addr = i2c_addr
        self._i2c_dev = i2c_dev
        self._drv8830 = Device(self._i2c_addr, i2c_dev=self._i2c_dev, registers=(
            Register('CONTROL', 0x00, fields=(
                BitField('voltage', 0b11111100, adapter=VoltageAdapter()),     # vset
                BitField('out2', 0b00000010),                                  # in2
                BitField('out1', 0b00000001),                                  # in1
                BitField('direction', 0b00000011, adapter=LookupAdapter({      # both in2 and in1 :D
                    'coast': 0b00,
                    'reverse': 0b01,
                    'forward': 0b10,
                    'brake': 0b11
                }))
            )),
            Register('FAULT', 0x01, fields=(
                BitField('clear', 0b10000000),             # Clears fault status bits when written to 1
                BitField('current_limit', 0b00010000),     # Fault caused by external current limit
                BitField('over_temperature', 0b00001000),  # Fault caused by over-temperature condition
                BitField('under_voltage', 0b00000100),     # Fault caused by undervoltage lockout
                BitField('over_current', 0b00000010),      # Fault caused by overcurrent event
                BitField('fault', 0b00000001)              # Fault condition exists
            ))
        ))

    def set_outputs(self, out1, out2):
        self._drv8830.set('CONTROL', out1=out1, out2=out2)

    def brake(self):
        self.set_direction('brake')

    def coast(self):
        self.set_direction('coast')

    def forward(self):
        self.set_direction('forward')

    def reverse(self):
        self.set_direction('reverse')

    def set_direction(self, direction):
        """Set the motor driver direction.

        Basically does the same thing as set_outputs, but takes
        a string name for directione, one of: coast, reverse,
        forward or brake.

        :param direction: string name of direction: coast, reverse, forward or brake

        """
        self._drv8830.set('CONTROL', direction=direction)

    def set_voltage(self, voltage):
        """Set the motor driver voltage.

        Roughly corresponds to motor speed depending upon the characteristics of your motor.

        :param voltage: from 0.48v to 5.06v

        """
        self._drv8830.set('CONTROL', voltage=voltage)

    def get_fault(self):
        """Get motor driver fault information.

        Returns a namedtuple of the fault flags:

        current_limit - external current limit exceeded (ilimit resistor), must clear fault or disable motor to reactivate
        over_temperature - driver has overheated, device resumes once temperature has dropped
        under_voltage - driver is below operating voltage (brownout), resumes once voltage has stabalised
        over_current - over-current protection activated, device disabled, must clear fault to reactivate
        fault - one or more fault flags is set

        """
        return self._drv8830.get('FAULT')

    def clear_fault(self):
        self._drv8830.set('FAULT', clear=True)
