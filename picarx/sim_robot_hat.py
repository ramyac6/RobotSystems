import os
import logging
from time import sleep
import time

class _Basic_class(object):
    _class_name = '_Basic_class'
    DEBUG_LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL,
              }
    DEBUG_NAMES = ['critical', 'error', 'warning', 'info', 'debug']

    def __init__(self):
        self._debug_level = 0
        self.logger = logging.getLogger(self._class_name)
        self.ch = logging.StreamHandler()
        form = "%(asctime)s	[%(levelname)s]	%(message)s"
        self.formatter = logging.Formatter(form)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)
        self._debug    = self.logger.debug
        self._info     = self.logger.info
        self._warning  = self.logger.warning
        self._error    = self.logger.error
        self._critical = self.logger.critical

    @property
    def debug(self):
        return self._debug_level

    @debug.setter
    def debug(self, debug):
        if debug in range(5):
            self._debug_level = self.DEBUG_NAMES[debug]
        elif debug in self.DEBUG_NAMES:
            self._debug_level = debug
        else:
            raise ValueError('Debug value must be 0(critical), 1(error), 2(warning), 3(info) or 4(debug), not \"{0}\".'.format(debug))  
        self.logger.setLevel(self.DEBUG_LEVELS[self._debug_level])
        self.ch.setLevel(self.DEBUG_LEVELS[self._debug_level])
        self._debug('Set logging level to [%s]' % self._debug_level)

    def run_command(self, cmd):
        import subprocess
        p = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = p.stdout.read().decode('utf-8')
        status = p.poll()
        # print(result)
        # print(status)
        return status, result

    def map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class fileDB(object):
	"""A file based database.
    A file based database, read and write arguements in the specific file.
    """
	def __init__(self, db:str, mode:str=None, owner:str=None):  
		'''Init the db_file is a file to save the datas.'''

		self.db = db
		# Check if db_file is existed, otherwise create one
		if self.db != None:	
			self.file_check_create(db, mode, owner)
		else:
			raise ValueError('db: Missing file path parameter.')


	def file_check_create(self, file_path:str, mode:str=None, owner:str=None):
		dir = file_path.rsplit('/',1)[0]
		try:
			if os.path.exists(file_path):
				if not os.path.isfile(file_path):
					print('Could not create file, there is a folder with the same name')
					return
			else:
				if os.path.exists(dir):
					if not os.path.isdir(dir):
						print('Could not create directory, there is a file with the same name')
						return
				else:
					os.makedirs(file_path.rsplit('/',1)[0], mode=0o754)
					sleep(0.001)

				with open(file_path, 'w') as f:
					f.write("# robot-hat config and calibration value of robots\n\n")

			if mode != None:
				os.popen('sudo chmod %s %s'%(mode, file_path))
			if owner != None:
				os.popen('sudo chown -R %s:%s %s'%(owner, owner, file_path.rsplit('/',1)[0]))		
		except Exception as e:
			raise(e) 
	
	def get(self, name, default_value=None):
		"""Get value by data's name. Default value is for the arguemants do not exist"""
		try:
			conf = open(self.db,'r')
			lines=conf.readlines()
			conf.close()
			file_len=len(lines)-1
			flag = False
			# Find the arguement and set the value
			for i in range(file_len):
				if lines[i][0] != '#':
					if lines[i].split('=')[0].strip() == name:
						value = lines[i].split('=')[1].replace(' ', '').strip()
						flag = True
			if flag:
				return value
			else:
				return default_value
		except FileNotFoundError:
			conf = open(self.db,'w')
			conf.write("")
			conf.close()
			return default_value
		except :
			return default_value
	
	def set(self, name, value):
		"""Set value by data's name. Or create one if the arguement does not exist"""

		# Read the file
		conf = open(self.db,'r')
		lines=conf.readlines()
		conf.close()
		file_len=len(lines)-1
		flag = False
		# Find the arguement and set the value
		for i in range(file_len):
			if lines[i][0] != '#':
				if lines[i].split('=')[0].strip() == name:
					lines[i] = '%s = %s\n' % (name, value)
					flag = True
		# If arguement does not exist, create one
		if not flag:
			lines.append('%s = %s\n\n' % (name, value))

		# Save the file
		conf = open(self.db,'w')
		conf.writelines(lines)
		conf.close()




class Servo(_Basic_class):
    MAX_PW = 2500
    MIN_PW = 500
    _freq = 50
    def __init__(self, pwm):
        pass

    # angle ranges -90 to 90 degrees
    def angle(self, angle):
        pass

    # pwm_value ranges MIN_PW 500 to MAX_PW 2500 degrees
    def set_pwm(self,pwm_value):
        pass

timer = [
    {
        "arr": 0
    }
] * 4

class I2C(_Basic_class):
    MASTER = 0
    SLAVE  = 1
    RETRY = 5

    def __init__(self, *args, **kargs):     # *args表示位置参数（形式参数），可无，； **kargs表示默认值参数，可无。
        pass

    def _i2c_write_byte(self, addr, data):   # i2C 写系列函数
        pass
    
    def _i2c_write_byte_data(self, addr, reg, data):
        pass
    
    def _i2c_write_word_data(self, addr, reg, data):
        pass
    
    def _i2c_write_i2c_block_data(self, addr, reg, data):
        pass
    
    def _i2c_read_byte(self, addr):   # i2C 读系列函数
        pass

    def _i2c_read_i2c_block_data(self, addr, reg, num):
        pass

    def is_ready(self, addr):
        pass

    def scan(self):                             # 查看有哪些i2c设备
        pass

    def send(self, send, addr, timeout=0):                      # 发送数据，addr为从机地址，send为数据
        pass

    def recv(self, recv, addr=0x00, timeout=0):     # 接收数据
        pass

    def mem_write(self, data, addr, memaddr, timeout=5000, addr_size=8): #memaddr match to chn
        pass
    
    def mem_read(self, data, addr, memaddr, timeout=5000, addr_size=8):     # 读取数据
        pass
    
    def readfrom_mem_into(self, addr, memaddr, buf):
        pass
    
    def writeto_mem(self, addr, memaddr, data):
        pass

class PWM(I2C):
    REG_CHN = 0x20
    REG_FRE = 0x30
    REG_PSC = 0x40
    REG_ARR = 0x44

    ADDR = 0x14

    CLOCK = 72000000

    def __init__(self, channel, debug="critical"):
        pass

    def i2c_write(self, reg, value):
        pass

    def freq(self, *freq):
        pass

    def prescaler(self, *prescaler):
        pass

    def period(self, *arr):
        pass

    def pulse_width(self, *pulse_width):
        pass

    def pulse_width_percent(self, *pulse_width_percent):
        pass



class Pin(_Basic_class):


    _dict = {
        "BOARD_TYPE": 12,
    }

    _dict_1 = {
        "D0":  17,
        "D1":  18,
        "D2":  27,
        "D3":  22,
        "D4":  23,
        "D5":  24,
        "D6":  25,
        "D7":  4,
        "D8":  5,
        "D9":  6,
        "D10": 12,
        "D11": 13,
        "D12": 19,
        "D13": 16,
        "D14": 26,
        "D15": 20,
        "D16": 21, 
        "SW":  19,
        "USER": 19,        
        "LED": 26,
        "BOARD_TYPE": 12,
        "RST": 16,
        "BLEINT": 13,
        "BLERST": 20,
        "MCURST": 21,

    }

    _dict_2 = {
        "D0":  17,
        "D1":   4, # Changed
        "D2":  27,
        "D3":  22,
        "D4":  23,
        "D5":  24,
        "D6":  25, # Removed
        "D7":   4, # Removed
        "D8":   5, # Removed
        "D9":   6,
        "D10": 12,
        "D11": 13,
        "D12": 19,
        "D13": 16,
        "D14": 26,
        "D15": 20,
        "D16": 21,     
        "SW":  25, # Changed
        "USER": 25,
        "LED": 26,
        "BOARD_TYPE": 12,
        "RST": 16,
        "BLEINT": 13,
        "BLERST": 20,
        "MCURST":  5, # Changed
    }

    def __init__(self, *value):
        pass
        
    def check_board_type(self):
        pass

    def init(self, mode, pull):
        pass

    def dict(self, *_dict):
        pass

    def __call__(self, value):
        return 1

    def value(self, *value):
        return 1

    def on(self):
        return 1

    def off(self):
        return 0

    def high(self):
        return self.on()

    def low(self):
        return self.off()

    def mode(self, *value):
        pass

    def pull(self, *value):
        return self._pull

    def irq(self, handler=None, trigger=None, bouncetime=200):
        pass

    def name(self):
        return "No GPIO"

    def names(self):
        return [self.name, self._board_name]

    class cpu(object):
        GPIO17 = 17
        GPIO18 = 18
        GPIO27 = 27
        GPIO22 = 22
        GPIO23 = 23
        GPIO24 = 24
        GPIO25 = 25
        GPIO26 = 26
        GPIO4  = 4
        GPIO5  = 5
        GPIO6  = 6
        GPIO12 = 12
        GPIO13 = 13
        GPIO19 = 19
        GPIO16 = 16
        GPIO26 = 26
        GPIO20 = 20
        GPIO21 = 21

        def __init__(self):
            pass


class Grayscale_Module(object):
    def __init__(self, pin0, pin1, pin2, reference=1000):
        pass

    def get_line_status(self,fl_list):
        return "no status"

    def get_grayscale_data(self):
        return []

class Ultrasonic():
    def __init__(self, trig, echo, timeout=0.02):
        self.trig = trig
        self.echo = echo
        self.timeout = timeout

    def _read(self):
        self.trig.low()
        time.sleep(0.01)
        self.trig.high()
        time.sleep(0.00001)
        self.trig.low()
        pulse_end = 0
        pulse_start = 0
        timeout_start = time.time()
        while self.echo.value()==0:
            pulse_start = time.time()
            if pulse_start - timeout_start > self.timeout:
                return -1
        while self.echo.value()==1:
            pulse_end = time.time()
            if pulse_end - timeout_start > self.timeout:
                return -1
        during = pulse_end - pulse_start
        cm = round(during * 340 / 2 * 100, 2)
        return cm

    def read(self, times=10):
        for i in range(times):
            a = self._read()
            if a != -1:
                return a
        return -1