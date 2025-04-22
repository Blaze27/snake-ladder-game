
class EntityFactory:
    @staticmethod
    def create_snake(start_cell, end_cell):
        from components.snake import Snake
        return Snake(start_cell=start_cell, end_cell=end_cell)
    
    @staticmethod
    def create_ladder(start_cell, end_cell):
        from components.ladder import Ladder
        return Ladder(start_cell=start_cell, end_cell=end_cell)
    
    @staticmethod
    def create_player(name, initial_position=0):
        from components.player import Player
        return Player(name=name, current_position=initial_position)