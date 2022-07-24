class Cell:
    def __init__(self, value):
        self.value = value
        self.left_neighbor = None 
        self.right_neighbor = None

    def move_to_right(self):
        if not self.right_neighbor:
            return 

        right = self.right_neighbor

        self.right_neighbor = right.right_neighbor
        if right.right_neighbor is not None:
            right.right_neighbor.left_neighbor = self

        right.left_neighbor = self.left_neighbor
        self.left_neighbor.right_neighbor = right

        right.right_neighbor = self 
        self.left_neighbor = right

    def should_move_to_right(self):
        if not self.right_neighbor:
            return False
        
        return self.value > self.right_neighbor.value 

    
