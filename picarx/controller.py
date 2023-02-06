import time

class Controller(object):
    def __init__(self,car,scale=30):
        self.scale = scale
        self.car = car
        self.running = False

    def control(self, offset):
        steering_angle = offset * self.scale
        self.car.set_dir_servo_angle(steering_angle)

    def consume(self, bus, delay):
        self.running = True
        while self.running:
            self.control(bus.read())
            time.sleep(delay)

