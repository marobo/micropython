import machine 
import time

led = machine.Pin(2, machine.Pin.OUT)


def micropy():
    for i in range(20):
        led.value(1)
        time.sleep_ms(500)
        led.value(0)
        time.sleep_ms(500)
micropy()
