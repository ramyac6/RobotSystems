from sensors import Sensors
from controller import Controller
from interpreter import Interpreter
try:
    from robot_hat import *
    from robot_hat import reset_mcu
    reset_mcu()
    time.sleep(0.01)
except ImportError:
    print("This computer does not appear to be a PiCar-X system (robot_hat is not present). Shadowing hardware calls with substitute functions ")
    from sim_robot_hat import *

def follow_line(self, scale = 50):
    sensor = Sensors()
    input("Press enter to calibrate grayscale, make sure all sensors are on black")

    sensor.calibrate_grayscale()

    # setup car things
    interpreter = Interpreter()
    car = Picarx()
    controller = Controller(car,scale)

    input("Press enter to start")

    while(True):
        controller.control(interpreter.calculate_direction(sensor.read()))
        time.sleep(0.1)