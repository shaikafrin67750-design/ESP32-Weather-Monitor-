```python
# ESP32 Weather Monitor
# MicroPython Program
# Sensor: DHT11 / DHT22

from machine import Pin
import dht
import time

# Connect DHT sensor data pin to GPIO 4
sensor = dht.DHT11(Pin(4))

print("ESP32 Weather Monitor")
print("---------------------")

while True:
    try:
        # Read temperature and humidity
        sensor.measure()

        temperature = sensor.temperature()
        humidity = sensor.humidity()

        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")

        if temperature > 35:
            print("Weather Status: HOT")
        elif temperature < 20:
            print("Weather Status: COOL")
        else:
            print("Weather Status: NORMAL")

        print("---------------------")
        time.sleep(2)

    except Exception as e:
        print("Sensor Error:", e)
        time.sleep(2)
```
