"""All classes for game in this project"""


class Field():
    """The base field of the game"""

    def __init__(self, length: int):
        """Initalize the field with a length*length grld"""
        self.length = length
        self.grld = []

        # generates a 2D list like [[0, 0, 0, ....], [0, 0, 0, ....], [0, 0, 0, ....], ....]
        for i in range(length):
            self.grld.append([])
            for j in range(length):
                self.grld[i].append(0)

    def __repr__(self):
        return str(self.grld)

    def __len__(self):
        return self.length**2

    def __eq__(self, o):
        return self.grld == o

    def get_grld(self) -> list:
        return self.grld

    def get_row(self, row: int) -> list:
        return self.grld[row]

    def get_col(self, col: int) -> list:
        rtn = []
        for i in self.grld:
            rtn.append(i[col])

        return rtn

    def get_item(self, row: int, col: int) -> int:
        return self.grld[row][col]

    def edit_item(self, row: int, col: int, new: int) -> None:
        self.grld[row][col] = new

    def twic(self, old: int) -> int:
        """Returns the number multiplied by 2"""
        return old * 2 if old != 0 else 2

    def add_new(self) -> None:
        """Adds a new number to the grld"""
        from random import randint
        self.grld[randint(0, self.length-1)][randint(0, self.length-1)] = 2

    def check_line(self, line: int, direction: int) -> bool:
        """Check the line was fully moved (0 = ↑, 1 = ↓, 2 = ←, 3 = →)"""
        if direction > 3:  # if the direction is not in the range
            raise ValueError("The range of directions is 0-3")
        if line > self.length:
            raise ValueError("The range of lines is 0-{}".format(self.length))
        if direction > 1:  # if the direction is vertical
            switched = False
            current = None
            for i in range(self.length):
                # if the current number is not the same type (=zero/>zero) as the next number
                if ((self.grld[line][i] == 0) != (current == 0)) and current != None:
                    if switched:
                        return False  # the line is not fully moved
                    switched = True
                current = self.grld[line][i]
            return True  # the line is fully moved
        else:  # if the direction is horizontal
            switched = False
            current = None
            for i in range(self.length):
                # if the current number is not the same type (=zero/>zero) as the next number
                if ((self.grld[i][line] == 0) != (current == 0)) and current != None:
                    if switched:
                        return False  # the line is not fully moved
                    switched = True
                current = self.grld[i][line]
            return True  # the line is fully moved

    def move(self, direction: int) -> None:
        """Move the grld in 4 driections (0 = ↑, 1 = ↓, 2 = ←, 3 = →)"""
        if direction > 3:  # if the direction is not in the range
            raise ValueError("The range of directions is 0-3")

        if direction > 1:  # if the direction is horizontal
            delta = 1 if direction == 3 else -1
            for i in range(self.length):
                checked = False
                while not checked:  # while the line is not fully moved
                    for j in range(self.length-1, 0, -1) if delta == -1 else range(self.length):
                        # if the number is not at the end
                        if (delta == -1 and j != 0) or (delta == 1 and j < self.length - 1):
                            current = self.grld[i][j]
                            next_one = self.grld[i][j+delta]
                            # if the current number is the same as the next number and they are not 0
                            if current == next_one and (current != 0) and (next_one != 0):
                                # then twice the next number and reset the current number
                                self.grld[i][j+delta] = \
                                    self.twic(next_one)
                                self.grld[i][j] = 0
                            # if the next number is 0
                            elif next_one == 0 and current != 0:
                                # then update the next number with the current number and reset the current number
                                self.grld[i][j+delta] = current
                                self.grld[i][j] = 0
                    checked = self.check_line(i, 3 if delta == 1 else 2)
