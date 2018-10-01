class Vehicle(object):
    #most important class

    def __init__(self):
        self.speed = 0
        self.size  = 0
        self.reckless = 0  # a parameter to define whether the drive is reckless or not
                        # from 0 to 1
        self.coodinate = (0,0) #place of a vehicle, (lane, mile)

    def change_lane(self, lane):
        #method to change to different lane
        pass



