from picarx_improved import Picarx


class Interpreter(object):
    def __init__(self,sensitivity=0.5,polarity=1):
        self.sensitivity = sensitivity * polarity

    def processing1(self, values):
        left, middle, right = values

        if right - left > 0: # means we're left of the line
            turn = -1 * (middle - right) / (middle + right)
        else:
            turn = -1 * (middle - right) / (middle + right)

        return turn * sensitivity

    def processing(self, values):
        # thresholds for marking
        similarity =
        difference = 

        # if left and middle are same and left and right are different
            # hard right
        # if righ tand middle are same and left and right are different 
            # slight right
        # if left and middle are same and left and right are different
            # light left
        # if right and middle are same and left and right are different 
            # hard left
        # if right and left are same and right is light
            # we're good
        # if right and left are same and right is light
            # uhhhhhh


if __name__ == "__main__":
    print()