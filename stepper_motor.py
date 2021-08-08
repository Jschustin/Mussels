import _thread
import time
import constants
from machine import Pin

_thread_is_running = False
_has_to_stop = False
_power = constants.STEPPER_MOTOR_LOW_POWER
_pin = Pin(constants.STEPPER_MOTOR_STEP_PIN, Pin.OUT)
_pin.value(0)

def _stepper_motor_runner():
    global _thread_is_running, _has_to_stop
    print("Thread started!")

    while True:
        if _has_to_stop:
            _pin.value(0)
            _thread_is_running = False
            print("Thread ended!!")
            return
        for _ in range(20):
            _pin.value(1)
            time.sleep(_power)
            _pin.value(0)
            time.sleep(_power)



def start_motor():
    global _thread_is_running
    if _thread_is_running:
        print("WARNING: Tried to start a thread already started!!")
        return
    _thread.start_new_thread(_stepper_motor_runner, ())
    _thread_is_running = True


def stop_motor():
    global _thread_is_running, _has_to_stop

    if not _thread_is_running:
        print("WARNING: Tried to stop a thread not running!")
        return

    _has_to_stop = True


def motor_set_power(p: float):
    """
    This function sets the power of the motor to p (-1 <= p <= 1).
    """
    global _power
    _power = p
