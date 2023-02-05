import time
from sensors import Sensors
from controller import Controller
from interpreter import Interpreter
from picarx_improved import Picarx


def follow_line(scale = 50):
    sensor = Sensors()
    input("Press enter to calibrate grayscale, make sure all sensors are on black")

    sensor.calibrate_grayscale()

    # setup car things
    interpreter = Interpreter()
    car = Picarx()
    controller = Controller(car,scale)

    input("Press enter to start")

    while(True):
        values = sensor.read()
        print(values)
        controller.control(interpreter.processing(values))
        time.sleep(0.1)

if __name__ == "__main__":
    follow_line()
