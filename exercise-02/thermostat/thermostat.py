class DigitalThermostat:
    def __init__(self, sensor, listener, temperature):
        self.sensor = sensor
        self.listener = listener
        self.temperature = temperature

    def check_temperature(self):
        current_temperature = self.sensor.getCurrentTemperature()
        if current_temperature < self.temperature:
            self.listener.onSignal(True)
        elif current_temperature > self.temperature:
            self.listener.onSignal(False)
