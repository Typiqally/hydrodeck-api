import logging

GPIO = None

try:
    import RPi.GPIO as GPIO
except ImportError:
    logging.warning(
        "Unable to import RPi.GPIO package, "
        "please install Raspberry Pi requirements using 'pip install -r pi-requirements.txt'"
    )

is_imported = GPIO is not None
