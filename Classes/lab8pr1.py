

class MilClock:
    
    def __init__(self, h, m):
        self.hours = h
        self.minutes = m

    def __str__(self):
        self.hoursStr = str(self.hours)
        self.minutesStr = str(self.minutes)
        if self.hours < 10 or len(self.hoursStr) == 1:
            self.hoursStr = "0" + str(self.hours)
        else:
            self.hoursStr = str(self.hours)
            self.minutesStr = str(self.minutes)
        if self.minutes < 10 or len(self.minutesStr) == 1:
            self.minutesStr = "0" + str(self.minutes)
        else:
            self.minutesStr = str(self.minutes)
        s = self.hoursStr + ":" + self.minutesStr
        return s

    def addOne(self):
        self.minutes += 1
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
        if self.hours == 24:
            self.hours = 0
