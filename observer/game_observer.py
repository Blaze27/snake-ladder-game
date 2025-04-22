from typing import Dict
from src.constants import Constants

class EventObserver:
    def notify(self, event_type, data: Dict):
        if event_type == Constants.SNAKE_ENCOUNTERED:
            print(f"{data['player_name']} encountered a snake! Moving down to {data['cell']}")
        elif event_type == Constants.LADDER_ENCOUNTERED:
            print(f"{data['player_name']} encountered a ladder! Moving up to {data['cell']}")