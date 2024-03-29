
"""All classes for game in this project"""


class Numbers():
    """Specfic the numbers in the game"""

    def __init__(self, power: int):
        self.val = 2**power if power != -1 else 0

    def __repr__(self):
        return self.val

    def __eq__(self, o):
        return int(self) == o

    def __ne__(self, o):
        return int(self) != o

    def __gt__(self, o):
        return int(self) > o

    def __lt__(self, o):
        return int(self) < o

    def __ge__(self, o):
        return int(self) >= o

    def __le__(self, o):
        return int(self) <= o

    def __int__(self):
        return int(self.val)

    def twic(self):
        self.val *= 2

    def update(self, new: int):
        self.val = new

    def reset(self):
        self.val = 0


class Field():
    """The base field of the game"""

    def __init__(self, length: int):
        """Initalize the field with a length*length grld"""
        self.length = length
        self.grld = list()

        # generates a 2D list like [[0, 0, 0, ....], [0, 0, 0, ....], [0, 0, 0, ....], ....] but type of 0 is classes.Numbers
        for i in range(length):
            self.grld.append([Numbers(-1)]*self.length)

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

    def edit_item(self, row: int, col: int, new: Numbers) -> None:
        self.grld[row][col] = new

    def move(self, direction: int):
        """Move the grld in 4 driections (0 = ↑, 1 = ↓, 2 = ←, 3 = →)"""
        if direction > 3:
            raise ValueError("The range of directions is 0-3")

        match direction:
            case 0:  # ^
                pass  # TODO:
            case 1:  # V
                pass
            case 2:  # ->
                for i in range(self.length):  # TODO: Make the numbers move
                    for j in range(0, self.length, -1):
                        if self.grld[i][j] == self.grld[i][j-1] and (self.grld[i][j] != 0) and (self.grld[i][j-1] != 0):
                            self.grld[i][j-1].twic()
                            self.grld[i][j].reset()
                        elif j < self.length:
                            if self.grld:  # TODO: Check if the number beside is 0
                                pass

            case 3:  # <-
                for i in range(self.length):  # TODO: Make the numbers move
                    for j in range(0, self.length):
                        if self.grld[i][j] == self.grld[i][j+1] and (self.grld[i][j] != 0) and (self.grld[i][j+1] != 0):
                            self.grld[i][j].twic()
                            self.grld[i][j+1].reset()
