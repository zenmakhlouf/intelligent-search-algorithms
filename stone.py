class Stone:
    def __init__(self,type):
        self.type = type

    def __str__(self):
        if self.type == "red":
            return "R"
        elif self.type == "purple":
            return "P"
        elif self.type == "metal":
            return "M"
        return "??"