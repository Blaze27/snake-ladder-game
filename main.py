from game.game_manager import GameManager

def get_inputs():
    """
    Get inputs for the game.
    :return: A tuple containing snakes, ladders, and players.
    """
    
    snakes = []
    ladders = []
    players = []

    num_snakes = int(input("Enter the number of snakes: "))
    for i in range(num_snakes):
        start, end = map(int, input(f"Enter the start and end positions of snake {i + 1}: ").split())
        snakes.append((start, end))

    num_ladders = int(input("Enter the number of ladders: "))
    for i in range(num_ladders):
        start, end = map(int, input(f"Enter the start and end positions of ladder {i + 1}: ").split())
        ladders.append((start, end))

    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        name = input(f"Enter the name of player {i + 1}: ")
        players.append(name)

    return snakes, ladders, players

def main():
    snakes, ladders, players = get_inputs()

    game_manager = GameManager(snakes=snakes, ladders=ladders, players=players)
    game_manager.start_game()
    
    
if __name__ == "__main__":
    main()