class Cell:
    def __init__(self, type, fill):
        self.type = type
        self.fill = fill

    def put_stone(self, stone):
        self.fill = stone

    def remove(self):
        self.fill = "empty"

    def change_type(self, type):
        self.type = type

    def is_empty(self):
        return self.fill == "empty"

    def toString(self):
        type_char = "G" if self.type == "goal" else "."
        fill_char = "." if self.fill == "empty" else str(self.fill)
        return f"{fill_char}{type_char}"

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        return self.type == other.type and self.fill == other.fill

    def __hash__(self):
        return hash((self.type, self.fill))

