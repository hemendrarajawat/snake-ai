from shared.direction import Direction
from shared.point import Point
from shared.game_state import GameState, GameStatus


# Test Direction Enum
def test_direction_enum():
    assert Direction.UP
    assert Direction.RIGHT
    assert Direction.DOWN
    assert Direction.LEFT


def test_direction_enum_is_unique():
    values = [d.value for d in Direction]
    assert len(values) == len(set(values))


# Test Point Object
def test_point_equality():
    p1 = Point(2, 3)
    p2 = Point(3, 4)
    p3 = Point(2, 3)

    assert p1 != p2
    assert p1 == p3


# Test Game State
def test_game_status_enum():
    assert GameStatus.MENU
    assert GameStatus.PLAYING
    assert GameStatus.PAUSED
    assert GameStatus.GAME_OVER


# Test GameState Object
def test_game_state_default_values():
    snake = [Point(1, 1), Point(1, 2), Point(1, 3)]
    food = Point(5, 5)

    game_state = GameState(snake=snake, direction=Direction.UP, food=food)

    assert game_state.snake == snake
    assert game_state.direction == Direction.UP
    assert game_state.food == food
    assert game_state.status == GameStatus.MENU
    assert game_state.score == 0


def test_game_state_custom_values():
    snake = [Point(5, 5), Point(5, 4)]
    food = Point(50, 50)

    game_state = GameState(
        snake=snake,
        direction=Direction.RIGHT,
        food=food,
        score=10,
        status=GameStatus.PLAYING,
    )

    assert game_state.snake == snake
    assert game_state.direction == Direction.RIGHT
    assert game_state.food == food
    assert game_state.status == GameStatus.PLAYING
    assert game_state.score == 10
