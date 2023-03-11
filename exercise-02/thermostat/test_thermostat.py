import unittest
from unittest.mock import Mock

from thermostat import DigitalThermostat

class TestDigitalThermostat(unittest.TestCase):
    def setUp(self):
        self.sensor = Mock()
        self.listener = Mock()

    def test_below_temperature(self):
        self.sensor.getCurrentTemperature.return_value = 20.0
        thermostat = DigitalThermostat(self.sensor, self.listener, 25.0)
        thermostat.check_temperature()
        self.listener.onSignal.assert_called_once_with(True)

    def test_above_temperature(self):
        self.sensor.getCurrentTemperature.return_value = 30.0
        thermostat = DigitalThermostat(self.sensor, self.listener, 25.0)
        thermostat.check_temperature()
        self.listener.onSignal.assert_called_once_with(False)

    def test_exact_temperature(self):
        self.sensor.getCurrentTemperature.return_value = 25.0
        thermostat = DigitalThermostat(self.sensor, self.listener, 25.0)
        thermostat.check_temperature()
        self.listener.onSignal.assert_not_called()

if __name__ == '__main__':
    unittest.main()
