import time
from sensors import Sensors
from controller import Controller
from interpreter import Interpreter
from picarx_improved import Picarx


def follow_line():
    sensor = Sensors()
    input("Press enter to calibrate grayscale, make sure all sensors are on white")

    sensor.calibrate_grayscale()

    # setup car things
    interpreter = Interpreter()
    car = Picarx()
    controller = Controller(car)

    input("Press enter to start")

    while(True):
        values = sensor.read()
        print(values)
        print([a/b for a,b in zip(values,sensor.grayscale_cal_values)])
        controller.control(interpreter.processing(values,sensor.grayscale_cal_values))
        car.forward(20)
        time.sleep(0.1)

if __name__ == "__main__":
    follow_line()
