from picarx_improved import Picarx


class Sensors(object):
    def __init__(self,pin0,pin1,pin2):
        self.chn0 = Picarx.ADC(pin0)
        self.chn1 = Picarx.ADC(pin1)
        self.chn2 = Picarx.ADC(pin2)

    def read(self):
        adc_value_list = []
        adc_value_list.append(self.chn0.read())
        adc_value_list.append(self.chn1.read())
        adc_value_list.append(self.chn2.read())
        return adc_value_list

if __name__ == "__main__":
    sensor = Sensors(0,1,2)
    print(sensor.read())

    
