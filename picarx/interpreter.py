from picarx_improved import Picarx


class Interpreter(object):
    def __init__(self,sensitivity=0.5,polarity=1):
        self.sensitivity = sensitivity * polarity

    def processing(self, values):
        values = [x+1 if x==0 else x for x in values]
        left, middle, right = values

        if right - left > 0: # means we're left of the line
            turn = -1 * (middle - right) / (middle + right)
        else:
            turn = (middle - left) / (middle + left)

        return turn * self.sensitivity

if __name__ == "__main__":
    print()
