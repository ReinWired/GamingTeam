class Board(list):
    def __init__(self, width, height):
        for i in range(height):
            self.append([False for j in range(width)])

board = Board(10, 5)