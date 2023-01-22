from picarx_improved import Picarx
import atexit
import time

class Maneuvering(object):
    def __init__(self):
        self.px = Picarx()
        #self.px = px
        self.default_speed = 40
        self.default_steering = 20
        self.max_steering = 40
        self.pause = 1
        self.command_wait = 0.25
        atexit.register(self.cleanup)

    def calibrate_steering(self):
        self.px.forward(self.default_speed)
        time.sleep(self.pause)
        self.px.stop()
    
    def forward_and_backward_with_steering(self):
        # take input
        valid = False
        forward_steer = input("Input forward steering angle: ")
        while not valid:
            try:
                forward_steer = int(forward_steer)
                valid = True
            except ValueError:
                forward_steer = input("Invalid number. Input forward steering angle: ")
            
        valid = False
        backward_steer = input("Input backward steering angle: ")
        while not valid:
            try: 
                backward_steer = int(backward_steer)
                valid = True
            except ValueError:
                backward_steer = input("Invalid number. Input backward steering angle: ")

        # forward
        self.px.set_dir_servo_angle(forward_steer)
        time.sleep(self.command_wait)
        self.px.forward(self.default_speed)
        time.sleep(self.pause)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)

        # backward
        self.px.set_dir_servo_angle(backward_steer)
        time.sleep(self.command_wait)
        self.px.backward(self.default_speed)
        time.sleep(self.pause)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)

    def parallel_parking(self):
        # take input
        valid = False
        side = input("Input parking side (left or right): ")
        while not valid:
            if side == "left" or side == "right":
                valid = True
            else:
                side = input("Invalid input. Input parking side (left or right): ")


        # assume side by side start 1in away
        # backwards
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)
        self.px.backward(self.default_speed)
        time.sleep(self.pause / 2)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)
        
        # back 45 into spot
        if side == "left":
            self.px.set_dir_servo_angle(-self.max_steering)
        else:
            self.px.set_dir_servo_angle(self.max_steering)
        time.sleep(self.command_wait)
        self.px.backward(self.default_speed)
        time.sleep(self.pause)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)

        # back in straight
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)
        self.px.backward(self.default_speed)
        time.sleep(self.pause / 2)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)

        # back 45 to parallel
        if side == "left":
            self.px.set_dir_servo_angle(self.max_steering)
        else:
            self.px.set_dir_servo_angle(-self.max_steering)
        time.sleep(self.command_wait)
        self.px.backward(self.default_speed)
        time.sleep(self.pause)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)

        # move forward into spot
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)
        self.px.forward(self.default_speed)
        time.sleep(self.pause / 1.5)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)

    def k_turn(self):
        # take input
        valid = False
        side = input("Input initial turning side (left or right): ")
        while not valid:
            if side == "left" or side == "right":
                valid = True
            else:
                side = input("Invalid input. Input initial turning side (left or right): ")

        # initial turn
        if side == "left":
            self.px.set_dir_servo_angle(-self.max_steering/2)
        else:
            self.px.set_dir_servo_angle(self.max_steering/2)
        time.sleep(self.command_wait)
        self.px.forward(self.default_speed)
        time.sleep(self.pause*2.5)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)

        # backup
        if side == "left":
            self.px.set_dir_servo_angle(self.max_steering/1.5)
        else:
            self.px.set_dir_servo_angle(-self.max_steering/1.5)
        time.sleep(self.command_wait)
        self.px.backward(self.default_speed)
        time.sleep(self.pause*1.7)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)

        # straighten
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)
        self.px.forward(self.default_speed)
        time.sleep(self.pause*1.5)
        self.px.stop()
        time.sleep(self.command_wait)
        self.px.set_dir_servo_angle(0)
        time.sleep(self.command_wait)

    def menu(self):
        while True:
            print("Welcome to the Picar menu!")
            print("0: Calibrate Steering")
            print("1: Forward and Backward (with steering")
            print("2: Parallel Parking")
            print("3: K-turn")
            print("q: Quit")

            menu_option = input("Please select a maneuver or q to quit: ")
            if menu_option == "0":
                maneuvering.calibrate_steering()
            elif menu_option == "1":
                maneuvering.forward_and_backward_with_steering()
            elif menu_option == "2":
                maneuvering.parallel_parking()
            elif menu_option == "3":
                maneuvering.k_turn()
            elif menu_option == "q":
                return
            else:
                print("Invalid Selection")

    def cleanup(self):
        self.px.set_dir_servo_angle(0)
        self.px.stop

if __name__ == "__main__":
    maneuvering = Maneuvering()
    maneuvering.menu()

    
