from typing import List, Optional
from components.player import Player
from factory.entity_factory import EntityFactory
from observer.game_observer import EventObserver
from src.constants import Constants


class GameManager:
    def __init__(self, snakes: List, ladders: List, players: List):
        """
        Initialize the game manager with a specified board size.
        :param board_size: The number of cells on the board (default is 10).
        """
        
        self.players = None
        self.winner: Player = None
        self.dice = None
        self.board = None
        self.next_player = None
        self.__initialize_game(snakes=snakes, ladders=ladders, players=players)

    def __initialize_game(self, 
                          snakes: Optional[List] = None, 
                          ladders: Optional[List] = None, 
                          players: Optional[List] = None
                          ):
        """
        Initialize the game with players, snakes, and ladders.
        """
        
        from components.board import Board
        from components.dice import Dice
        
        self.board = Board()
        self.__create_snakes(snakes=snakes)
        self.__create_ladders(ladders=ladders)
        self.players = self.__create_players(players=players)
        self.dice = Dice()
        self.observers = { Constants.EVENT_OBSERVER: EventObserver() }

    def __observer_notify(self, observer_key, event_type, data):
        observer = self.observers.get(observer_key)
        if observer:
            observer.notify(event_type=event_type, data=data)
        else:
            print("No observer key has found")
    
    def __create_players(self, players: List):
        """
        Create players for the game.
        :param players: A list of player names.
        :return: A list of Player objects.
        """

        initial_position = 0
        return [EntityFactory.create_player(name, initial_position) for name in players]
    
    def __create_snakes(self, snakes: List):
        """
        Create snakes for the game.
        :param snakes: A list of tuples representing snake x and y positions.
        """
        
        for start, end in snakes:
            snake = EntityFactory.create_snake(start, end)
            self.board.add_snake(snake)
    
    def __create_ladders(self, ladders: List):
        """
        Create ladders for the game.
        :param ladders: A list of tuples representing ladder x and y positions.
        """
        
        for start, end in ladders:
            ladder = EntityFactory.create_ladder(start_cell=start, end_cell=end)
            self.board.add_ladder(ladder)

    def start_game(self):
        """
        Start the game and manage the turns of players.
        """
        
        while not self.winner:
            self.__play_turn()
        
        print(f"Game Over! The winner is {self.winner.name}.")
    
    def __check_for_snake_or_ladder(self, player: Player):
        """
        Check if the player has landed on a snake or ladder.
        """
        
        current_position = player.get_position()
        
        for snake in self.board.snakes:
            if current_position == snake.start_cell:
                self.__observer_notify(Constants.EVENT_OBSERVER, Constants.SNAKE_ENCOUNTERED, data={'player_name': player.name, 'cell': snake.end_cell})
                player.move(snake.end_cell)
                return
        
        for ladder in self.board.ladders:
            if current_position == ladder.start_cell:
                self.__observer_notify(Constants.EVENT_OBSERVER, Constants.LADDER_ENCOUNTERED, data={'player_name': player.name, 'cell': ladder.end_cell})
                player.move(ladder.end_cell)
                return
    
    def __play_turn(self):
        """
        Play a turn for the current player.
        """
        
        if self.next_player is None:
            self.next_player = self.players[0]
        
        current_player = self.next_player
        input("Press Enter to roll the dice...")
        roll = self.dice.roll()
        print(f"{current_player.name} rolled a {roll}.")
        current_player.move(current_player.current_position + roll)

        self.__check_for_snake_or_ladder(current_player)
        if self.__check_for_winner(current_player):
            return
        self.__next_player()
    
    def __check_for_winner(self, player: Player):
        """
        Check if the player has reached the end of the board.
        """
        
        if player.current_position >= self.board.board_size:
            self.winner = player
            print(f"{player.name} has won the game!")
            return True
        return False
    
    def __next_player(self):
        """
        Move to the next player in the list.
        """
        
        current_index = self.players.index(self.next_player)
        next_index = (current_index + 1) % len(self.players)
        self.next_player = self.players[next_index]
        print(f"Next player is {self.next_player.name}.")

        