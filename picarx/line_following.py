import time
from sensors import Sensors
from controller import Controller
from interpreter import Interpreter
from picarx_improved import Picarx
from bus import Bus
import concurrent.futures


def follow_line():
    sensor = Sensors()
    input("Press enter to calibrate grayscale, make sure all sensors are on white")

    sensor.calibrate_grayscale()

    # setup car things
    interpreter = Interpreter()
    car = Picarx()
    controller = Controller(car)
    # setup busses
    interpreter_bus = Bus()
    sensor_bus = Bus()
    delay = 0.05

    input("Press enter to start")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        eSensor = executor.submit(sensor.produce, sensor_bus, delay)
        eInterpreter = executor.submit(interpreter.produce_consume, sensor_bus, interpreter_bus, delay)
        eController = executor.submit(controller.consume, interpreter_bus, delay)

    eSensor.result()
    eInterpreter.result()
    eController.result()


if __name__ == "__main__":
    follow_line()
