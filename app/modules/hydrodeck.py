import app.config as config
import app.modules.gpio as gpio

GPIO = gpio.GPIO

output_pins = [
    config.OPEN_GPIO_PIN,
    config.CLOSE_GPIO_PIN,
    config.STOP_GPIO_PIN,
]


def setup():
    GPIO.setmode(GPIO.BCM)

    for pin in output_pins:
        setup_output(pin)


def setup_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def get_status():
    return {
        "is_controllable": gpio.is_imported
    }


if gpio.is_imported:
    setup()
