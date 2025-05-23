import esp32
from umqtt.simple import MQTTClient
import machine
from machine import Pin, Timer
import uasyncio as asyncio
import network
import usocket
import utime
import ujson
import usocket as socket
import ntptime
import time



# Pin Setup
R1 = Pin(26, Pin.OUT)
R2 = Pin(25, Pin.OUT)
R3 = Pin(33, Pin.OUT)

S_Led = Pin(4, Pin.OUT)


Rst = Pin(32, Pin.IN, Pin.PULL_UP)

press_start_time = None
debounce_timer = Timer(2)
reset_timer = Timer(1)

async def http_server_led():
    for _ in range(3):
        S_Led.value(1)
        await asyncio.sleep(1)
        S_Led.value(0)
        await asyncio.sleep(1)

    
async def blink_reconnect():
    for _ in range(3):
        S_Led.value(1)
        await asyncio.sleep(0.5)
        S_Led.value(0)
        await asyncio.sleep(0.5)




