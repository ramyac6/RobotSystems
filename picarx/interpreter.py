import time
from bus import Bus

class Interpreter(object):
    def __init__(self,sensitivity=0.1,polarity=1):
        self.sensitivity = sensitivity * polarity
        self.running = False

    def processing(self, values, cal_values):
        values = [x+1 if x == 0 else x for x in values]
        left, middle, right = values

        left, middle, right = values
        left_cal, middle_cal, right_cal = cal_values
        left = left/left_cal
        middle = middle/middle_cal
        right = right/right_cal

        if abs(right - left) > self.sensitivity: # means we're off the line
            if right > left:
                print("left")
                turn = (left - middle) / (middle+left)
            else: # left > right:
                turn = (middle - right) / (middle+right)
        else: # we're perfect
            turn = 0

        return turn

    def produce_consume(self, sensor_bus: Bus, interpreter_bus: Bus, delay):
        self.running = True
        while self.running:
            message = sensor_bus.read()
            value = self.processing(message)
            interpreter_bus.write(value)
            time.sleep(delay)

