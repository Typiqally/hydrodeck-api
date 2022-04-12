import logging

is_controllable = False

try:
    import RPi.GPIO as GPIO
    import app.config as config

    output_pins = [
        config.OPEN_GPIO_PIN,
        config.CLOSE_GPIO_PIN,
        config.STOP_GPIO_PIN,
    ]

    # Update controllable status
    is_controllable = True


    def setup():
        GPIO.setmode(GPIO.BCM)

        for pin in output_pins:
            setup_output(pin)


    def setup_output(pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)


    setup()

except ImportError:
    logging.warning("Unable to import RPi.GPIO package, "
                    "please install Raspberry Pi requirements using 'pip install -r pi-requirements.txt'")


def get_status():
    return {
        "is_controllable": is_controllable
    }
