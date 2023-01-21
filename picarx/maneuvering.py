from picarx_improved import Picarx
import atexit

class Maneuvering(object):
    def __init__(self):
        self.px = Picarx()
        atexit.register(self.cleanup)

    def calibrate_steering(self):
        self.px.forward(50)
        self.time.sleep(1)
        self.px.stop()

    def cleanup(self):
        self.px.stop