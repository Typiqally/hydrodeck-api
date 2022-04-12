import app.config as config
import app.modules.gpio as gpio

GPIO = gpio.GPIO

action_pins = {
    0: config.CLOSE_GPIO_PIN,
    1: config.OPEN_GPIO_PIN,
    2: config.CLOSE_GPIO_PIN,
}


def setup():
    GPIO.setmode(GPIO.BCM)

    for action in action_pins:
        GPIO.setup(action_pins[action], GPIO.OUT)

    reset_output()


def reset_output():
    for pin in action_pins:
        GPIO.output(pin, GPIO.LOW)


def execute_action(action: int):
    if not gpio.is_imported or action not in action_pins:
        return False

    reset_output()
    GPIO.output(action_pins.get(action), GPIO.HIGH)

    return True


def get_status():
    return {
        "connected": gpio.is_imported
    }


if gpio.is_imported:
    setup()
