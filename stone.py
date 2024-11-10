class Stone:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return {"red": "R", "purple": "P", "metal": "M"}.get(self.type, "??")

    def __eq__(self, other):
        if not isinstance(other, Stone):
            return False
        return self.type == other.type

    def __hash__(self):
        return hash(self.type)