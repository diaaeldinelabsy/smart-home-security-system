# Smart Home Security System

This is a security system using Raspberry Pi, motion and distance sensors, LEDs, a buzzer, and Telegram alerts.

## Features
- Detects motion using PIR sensor
- Measures distance with ultrasonic sensor
- Shows LED status:
  - Green = idle
  - Yellow = motion detected
  - Red + buzzer = object too close
- Sends Telegram alert if object < 30 cm

## Hardware Used
- Raspberry Pi
- PIR motion sensor
- Ultrasonic sensor (HC-SR04)
- 3 LEDs (green, yellow, red)
- Buzzer
- Breadboard + Jumper wires

## Software
- Python
- Libraries: `RPi.GPIO`, `requests`, `time`

## Skills Learned
- GPIO control
- Real-time sensor reading
- Embedded system design
- Telegram API integration
