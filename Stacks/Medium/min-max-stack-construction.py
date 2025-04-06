# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.data = []
        self.mines = []
        self.maxes = []

    def peek(self):
        # Write your code here.
        return self.data[-1]

    def pop(self):
        # Write your code here.
        self.mines.pop()
        self.maxes.pop()

        return self.data.pop()

    def push(self, number):
        # Write your code here.
        self.data.append(number)
        if len(self.mines) == 0 :
            self.mines.append(number)
        else:
            self.mines.append(min(self.mines[-1], number))

        if len(self.maxes) == 0 :
            self.maxes.append(number)
        else:
            self.maxes.append(max(self.maxes[-1], number))

        return

    def getMin(self):
        # Write your code here.
        return self.mines[-1]

    def getMax(self):
        # Write your code here.
        return self.maxes[-1]
