from RPi import GPIO
import sys

PIN = 24

GPIO.setmode(GPIO.BCM)
# NB: This script will re-setup the pin each time
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)


def on(pin=PIN):
    GPIO.output(pin, 1)


def off(pin=PIN):
    GPIO.output(pin, 0)


if __name__ == '__main__':
    if sys.argv[1] == 'on':
        on()
    elif sys.argv[1] == 'off':
        off()
    else:
        raise ValueError('Unrecognized argument: {}'.format(sys.argv[1]))
