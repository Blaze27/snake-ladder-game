class Player:
    def __init__(self, name: str, current_position: int):
        self.name = name
        self.current_position = current_position
    
    def move(self, new_position: int):
        result = self.__set_position(new_position)
        return result

    def get_position(self):
        print(f"Player {self.name} is at position {self.current_position}")
        return self.current_position
    
    def __set_position(self, new_position: int):
        self.current_position = new_position
        print(f"Player {self.name} moved to position {self.current_position}")
