from enum import Enum


class Constants(Enum):
    """
    Constants used in the application.
    """

    # API constants
    OCCUPIED = "OCCUPIED"
    UN_OCCUPIED = "UNOCCUPIED"
    EVENT_OBSERVER = "EVENT_OBSERVER"
    SNAKE_ENCOUNTERED = "SNAKE_ENCOUNTERED"
    LADDER_ENCOUNTERED = "LADDER_ENCOUNTERED"