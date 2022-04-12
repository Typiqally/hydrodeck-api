import logging

is_controllable = False

try:
    import RPi.GPIO as GPIO
    import app.config as config

    # Update controllable status
    is_controllable = True

except ImportError:
    logging.warning("Unable to import RPi.GPIO package, "
                    "please install Raspberry Pi requirements using 'pip install -r pi-requirements.txt'")


def get_status():
    return {
        "is_controllable": is_controllable
    }
