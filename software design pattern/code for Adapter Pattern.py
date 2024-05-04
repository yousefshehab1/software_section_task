# Adaptee - The existing class or interface that needs to be adapted
class FahrenheitSensor:
    def get_temperature(self):
        temperature = 99.5  # Simulated temperature reading
        return temperature


# Target - The desired interface that the client code expects
class CelsiusSensor:
    def get_temperature(self):
        return 0


# Adapter - Adapts the interface of the Adaptee to the Target interface
class TemperatureAdapter:
    def __init__(self, sensor):
        self.sensor = sensor

    def get_temperature(self):
        fahrenheit_temp = self.sensor.get_temperature()
        # Convert Fahrenheit to Celsius
        celsius_temp = (fahrenheit_temp - 32) * 5 / 9
        return celsius_temp


# Client code
def main():
    fahrenheit_sensor = FahrenheitSensor()
    adapter = TemperatureAdapter(fahrenheit_sensor)
    print("Temperature in Celsius:", adapter.get_temperature())


if __name__ == "__main__":
    main()
