#This program will calculate a relative wind angle to a plane.                                                                    
class RelativeWindCalculator(object):
    version = '1.1'

    def __init__(self):
        self.relative = ()

    def inputnumbers(self, wh, ph):
        if wh  != int() or ph != int():
            raise Exception('Only numbers can be input')
            self.relative()

    def incorrecthandling(self, wh, ph):
        if wh  > 360 or ph > 360 or wh < 0 or ph < 0:
            raise Exception('Input correct handling - from 0 to 360 degree')
            self.relative()

    def windcalculator(self, wh, ph):

        relative = ph - wh
        if relative > 180:
            self.relative = relative - 360

        if relative < -180:
            self.relative = 360 + relative

        if relative <= 180 and relative >= -180:
            self.relative = relative

        return relative



