def main():
    print("Hello")

class Room:
    def __init__(self, num, type, is_occupied = False):
        self.roomNumber = num
        self.roomType = type
        self.isOccupied = is_occupied

    @property
    def roomNumber(self):
        return self.roomNumber
    @property
    def roomType(self):
        return self.roomType
    @property
    def isOccupied(self):
        return self.isOccupied
    
    @roomNumber.setter
    def roomNumber(self, num):
        self.roomNumber = num
    @roomType.setter
    def roomType(self, type):
        self.roomType = type
    @isOccupied.setter
    def isOccupied(self, occup):
        self.isOccupied = occup

    


    
