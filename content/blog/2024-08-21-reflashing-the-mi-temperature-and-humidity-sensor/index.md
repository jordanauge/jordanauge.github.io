---
title: Reflashing the Mi Temperature and Humidity Sensor
date: 2024-08-21
slug: reflashing-the-mi-temperature-and-humidity-sensor
status: draft
---

from bluetooth to BTLE
now supports zigbee

Xiaomi Mijia (LYWSD03MMC)

first that got open, but other models are supported
see: Adjustable RF TX Power (-20..+10dB) & Bluetooth advertising interval. +3..+10 dB require a more powerful power supply.
nicest design, display for local use
not the best, but correct battery life

https://github.com/atc1441/ATC_MiThermometer

https://github.com/pvvx/ATC_MiThermometer
https://pvvx.github.io/ATC_MiThermometer/

BTHome


## move to zigbee

https://github.com/devbis/z03mmc

https://github.com/pvvx/ZigbeeTLc
    more recent, same guy as BLE version, advertise power consumption, close to BT one

BT
    Using the default settings for advertising interval of 2.5 seconds and measurement interval of 10 seconds:
    Bluetooth Advertisement: 14..15 uA 3.3V (CR2032 over 1 years)
Z
    Average consumption for Xiaomi LYWSD03MMC HW: B1.4 - ~15 uA.

## DL

To build the custom firmware on your own, follow this guide to get a working TC32 Compiler environment ready where you can add the Custom Mi firmware.
Original guide in Chinese: https://github.com/Ai-Thinker-Open/Telink_825X_SDK
