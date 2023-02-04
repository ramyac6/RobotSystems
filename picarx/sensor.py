import time
try:
    from robot_hat import *
    from robot_hat import reset_mcu
    reset_mcu()
    time.sleep(0.01)
except ImportError:
    print("This computer does not appear to be a PiCar-X system (robot_hat is not present). Shadowing hardware calls with substitute functions ")
    from sim_robot_hat import *

class Sensors(object):
    def __init__(self,pin0,pin1,pin2):
        # grayscale sensors
        self.chn0 = Picarx.ADC('A0')
        self.chn1 = Picarx.ADC('A1')
        self.chn2 = Picarx.ADC('A2')

    def read(self):
        adc_value_list = []
        adc_value_list.append(self.chn0.read())
        adc_value_list.append(self.chn1.read())
        adc_value_list.append(self.chn2.read())
        return adc_value_list

if __name__ == "__main__":
    sensor = Sensors("A0","A1","A2")
    x = 0
    while (x < 1000000):
        time.sleep(0.5)
        print(sensor.read())
        x = x + 0.1
