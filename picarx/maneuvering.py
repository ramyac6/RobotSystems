from picarx_improved import Picarx
import atexit
import time

class Maneuvering(object):
    def __init__(self):
        self.px = Picarx()
        atexit.register(self.cleanup)

    def calibrate_steering(self):
        self.px.forward(50)
        time.sleep(1)
        self.px.stop()

    def cleanup(self):
        self.px.stop

if __name__ == "__main__":
    maneuvering = Maneuvering()
    maneuvering.calibrate_steering()