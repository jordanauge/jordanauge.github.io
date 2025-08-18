---
title: Repair techniques
date: 2024-09-17
slug: repair-techniques
status: unpublished
---

## First tasks

Disconnect everything
Power supply check

## Board inspection

Understanding principal components

### Power rails

PC : mostly power rails 12V 3V 5V 1.1V 0.8V
Switching power supply

VRM = voltage regulation management

The circuit responsible for controlling the mosfets

TODO : schema with 2 3 mosfets

will guide a lot the tests we do later for shorts

### Embedded Controller (EC)

resposible for computer bootup
guide the boot process of a computer (eg. if it switches down)


## Searching for short

Measure resistance
Typical values are indicative of MOSFET / Capacitors in short
low resistance : newer CPUs, don't confuse with short

Capacitors always connect + and -
should never be in shortcut

MOSFETS
1 pin to ground
low side, high side
N versus P : todo
pins should never be shortcut

## Thermal camera

## Injecting voltage

1 V max until we are sure there is no high side short
otherwise injecting voltage directly into possibly sensitie components, eg.
CPU/GPU
max current ? 500mA ? enough to cause a component to heat

should be proportional to the short resistance


