class Cell:
    def __init__(self,type,fill):
        self.type = type
        self.fill = fill

    def put_stone(self,stone):
        self.fill = stone
    def remove(self):
        self.fill = "empty"
    def change_type(self,type):
        self.type = type
    def is_empty(self):
        if(self.fill == "empty"):
            return True
        else:
            return False
    def toString(self):
        # Get cell type indicator
        if self.type == "goal":
            type_char = "G"
        else:
            type_char = "."
        
        # Get fill indicator
        if self.fill == "empty":
            fill_char = "."
        else:
            fill_char = str(self.fill)
        
        # Combine them (fill first, then type)
        return f"{fill_char}{type_char}"
        
# type [blank, goal, unreachable ]
# fill[Stone,Empty]