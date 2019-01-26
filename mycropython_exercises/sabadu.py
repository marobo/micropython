>>> import machine
>>> led = machine.Pin(2, machine.Pin.OUT)
>>> for i in range(20):
...     led.value(1)
...     time.sleep_ms(500)
...     led.value(0)
...     time.sleep_ms(500)
...     
...     
... 
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
NameError: name 'time' is not defined
>>> for i in range(20):
...     led.value(1)
...     time.sleep_ms(500)
...     led.value(0)
...     time.sleep_ms(500)
...     
...     
... 
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
NameError: name 'time' is not defined
>>> led.value(1)
>>> led.value(0)
>>> 
>>> 
>>> for i in range(20):
...     led.value(1)
...     time.sleep_ms(500)
...     led.value(0)
...     time.sleep_ms(500)
...     
...     
... 
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
NameError: name 'time' is not defined
>>> 
>>> import network
>>> wlan.scan()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wlan' is not defined
>>> 
>>> 
>>> sta_if = network.WLAN(network.STA_IF)
>>> ap_if = network.WLAN(network.AP_IF)
>>> sta_if.active()
False
>>> ap_if.active()
True
>>> ap_if.ifconfig()
('192.168.4.1', '255.255.255.0', '192.168.4.1', '208.67.222.222')
>>> wla.active()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wla' is not defined
>>> wlan.active()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wlan' is not defined
>>> 
>>> 
>>> 
>>> wlan = network.WLAN(network.STA_IF)
>>> wlan.active()
False
>>> wlan.ifconfig()
('0.0.0.0', '0.0.0.0', '0.0.0.0', '208.67.222.222')
>>> wlan.scan()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: STA must be active
>>> 
>>> 
>>> wlan.active(True)
#5 ets_task(4020ed88, 28, 3fff9ea8, 10)
>>> wlan.scan()
[(b'MicroPython-0385fb', b'^\xcf\x7f\x03\x85\xfb', 1, -41, 4, 0), (b'MicroPython-022a07', b'b\x01\x94\x02*\x07', 1, -46, 4, 0), (b'CatalpaLAN', b'\x02%\x9c\x13\xfc\xc9', 1, -44, 3, 0), (b'Catalpa', b'\x00%\x9c\x13\xfc\xc9', 1, -52, 3, 0), (b'motaboot', b'\x06%\x9c\x13\xfc\xc9', 1, -43, 3, 0)]
>>> 
