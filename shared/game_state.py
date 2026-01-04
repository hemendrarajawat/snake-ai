from enum import Enum
from shared.point import Point
from shared.direction import Direction


class GameStatus(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"


class GameState:
    def __init__(
        self,
        snake: list[Point],
        direction: Direction,
        food: Point,
        score: int = 0,
        status: GameStatus = GameStatus.MENU,
    ):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.score = score
        self.status = status
