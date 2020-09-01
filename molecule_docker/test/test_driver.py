"""Unit tests."""
from molecule import api

# from . import DRIVER


def test_driver_is_detected(DRIVER):
    """Asserts that molecule recognizes the driver."""
    assert DRIVER in [str(d) for d in api.drivers()]
