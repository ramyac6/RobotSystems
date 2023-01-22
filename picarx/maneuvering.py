from picarx_improved import Picarx
import atexit
import time

class Maneuvering(object):
    def __init__(self):
        self.px = Picarx()
        #self.px = px
        self.default_speed = 40
        self.default_steering = 20
        self.pause = 1
        self.command_wait = 0.25
        atexit.register(self.cleanup)

    def calibrate_steering(self):
        self.px.forward(self.default_speed)
        time.sleep(self.pause)
        self.px.stop()
    
    def forward_and_backward_with_steering(self, forward_steer, backward_steer):
        # forward
        self.px.set_dir_servo_angle(forward_steer)
        time.sleep(self.command_wait)
        self.px.forward(self.default_speed)
        time.sleep(self.pause)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)
        self.command_wait

        # backward
        self.px.set_dir_servo_angle(backward_steer)
        time.sleep(self.command_wait)
        self.px.backward(self.default_speed)
        time.sleep(self.pause)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)

    def cleanup(self):
        self.px.set_dir_servo_angle(0)
        self.px.stop

if __name__ == "__main__":
    maneuvering = Maneuvering()
    # maneuvering.calibrate_steering()
    maneuvering.forward_and_backward_with_steering(20,-20)