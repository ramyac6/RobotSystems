from picarx_improved import Picarx


class Controller(object):
    def __init__(self,car,scale):
        self.scale = scale
        self.car = car

    def control(self,angle, speed=20):
        self.car.drive(speed, angle*self.scale)

if __name__ == "__main__":
    print()