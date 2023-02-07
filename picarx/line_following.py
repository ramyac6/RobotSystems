import time
from grayscale import Grayscale_Sensor, Grayscale_Controller, Grayscale_Interpreter
from picarx_improved import Picarx
from rossros import Bus
import concurrent.futures


def follow_line():
    gs_sensor = Grayscale_Sensor()
    input("Press enter to calibrate grayscale, make sure all sensors are on white")

    gs_sensor.calibrate_grayscale()

    # setup car things
    interpreter = Grayscale_Interpreter()
    car = Picarx()
    controller = Grayscale_Controller(car)
    # setup busses
    interpreter_bus = Bus(name="interpreter_bus")
    sensor_bus = Bus(name="sensor_bus")
    delay = 0.05

    input("Press enter to start")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        eSensor = executor.submit(gs_sensor.produce, sensor_bus, delay)
        eInterpreter = executor.submit(interpreter.produce_consume, sensor_bus, interpreter_bus, delay)
        eController = executor.submit(controller.consume, interpreter_bus, delay)

    eSensor.result()
    eInterpreter.result()
    eController.result()


if __name__ == "__main__":
    follow_line()
