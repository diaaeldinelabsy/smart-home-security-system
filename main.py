# ------------------------------------------------------------
# Project: Smart Home Security System using Raspberry Pi
# Author: DiaaEldin Elabsy
# Date: (Apr–Jun) 2025 
# Description:
# This program monitors motion using a PIR sensor and checks proximity
# using an ultrasonic sensor. If motion is detected and the object is
# too close (<30 cm), it triggers a red LED, buzzer, and sends a 
# Telegram alert. LEDs indicate system status (green = idle,
# yellow = motion, red = alert).
# ------------------------------------------------------------

import RPi.GPIO as GPIO
import time
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pins define
PIR = 17
TRIG = 23
ECHO = 24
Green_LED = 6
Yellow_LED = 5
Red_LED = 13
Buzzer = 18

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(Green_LED, GPIO.OUT)
GPIO.setup(Yellow_LED, GPIO.OUT)
GPIO.setup(Red_LED, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)

BOT_TOKEN = '7531609808:AAH4QKpy1_OD93v_GDpG8byGoJ1-yijaCDY'
CHAT_ID = '6066572474'

def send_telegram_alert():
    message = "Diaa motion detected! Someone is too close to the door."
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
        print("Telegram alert sent.")
    except:
        print("Failed to send Telegram alert.")

def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    dist = (TimeElapsed * 34300) / 2
    return dist

try:
    motion = True

    while True:
        if GPIO.input(PIR):
            motion = False
            GPIO.output(Green_LED, False)
            GPIO.output(Yellow_LED, True)
            time.sleep(2)
            GPIO.output(Yellow_LED, False)

            dist = distance()
            print(f"Distance after wait: {dist} cm")

            if dist < 30:
                GPIO.output(Red_LED, True)
                GPIO.output(Buzzer, True)
                send_telegram_alert()
                time.sleep(2)
                GPIO.output(Buzzer, False)
                GPIO.output(Red_LED, False)
            else:
                GPIO.output(Green_LED, True)
                GPIO.output(Yellow_LED, False)
                GPIO.output(Red_LED, False)
                GPIO.output(Buzzer, False)

except KeyboardInterrupt:
    GPIO.cleanup()
