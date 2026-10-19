"""Snake and Ladder Game: Complete object-oriented turn-based game loop."""

from collections import deque
import random
from typing import Dict, List, Optional


# 1. Obstacle Hierarchy (Snake & Ladder)
class Obstacle:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


class Snake(Obstacle):
    def __init__(self, head: int, tail: int) -> None:
        if head <= tail:
            raise ValueError("Snake head must be at a higher cell than tail.")
        super().__init__(head, tail)


class Ladder(Obstacle):
    def __init__(self, bottom: int, top: int) -> None:
        if bottom >= top:
            raise ValueError("Ladder bottom must be at a lower cell than top.")
        super().__init__(bottom, top)


# 2. Board
class Board:
    def __init__(self, size: int = 100) -> None:
        self.size = size
        self.obstacles: Dict[int, int] = {}  # start_cell -> end_cell

    def add_snake(self, head: int, tail: int) -> None:
        self.obstacles[head] = tail

    def add_ladder(self, bottom: int, top: int) -> None:
        self.obstacles[bottom] = top

    def get_final_position(self, current_pos: int) -> int:
        # Check if cell lands on a Snake or Ladder
        if current_pos in self.obstacles:
            dest = self.obstacles[current_pos]
            if dest < current_pos:
                print(f"    🐍 Bitten by Snake at {current_pos}! Slid down to {dest}.")
            else:
                print(f"    🪜 Climbed Ladder at {current_pos}! Climbed up to {dest}.")
            return dest
        return current_pos


# 3. Dice
class Dice:
    def __init__(self, min_val: int = 1, max_val: int = 6) -> None:
        self.min_val = min_val
        self.max_val = max_val

    def roll(self) -> int:
        return random.randint(self.min_val, self.max_val)


# 4. Player
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.position = 0  # Starts off the board


# 5. Game Controller
class SnakeAndLadderGame:
    def __init__(self, board: Board, dice: Dice, player_names: List[str]) -> None:
        self.board = board
        self.dice = dice
        self.players: deque[Player] = deque([Player(name) for name in player_names])
        self.winner: Optional[Player] = None

    def play_turn(self) -> bool:
        if self.winner:
            return True

        current_player = self.players.popleft()
        roll = self.dice.roll()
        target_pos = current_player.position + roll

        print(f"[{current_player.name}] Rolled a {roll}. Current: {current_player.position} -> Target: {target_pos}")

        if target_pos > self.board.size:
            print(f"  Overshot cell {self.board.size}! Turn skipped.")
            self.players.append(current_player)
            return False

        # Apply board obstacles (snakes/ladders)
        final_pos = self.board.get_final_position(target_pos)
        current_player.position = final_pos
        print(f"  Moved to cell {current_player.position}")

        # Check win condition
        if current_player.position == self.board.size:
            self.winner = current_player
            print(f"\n🏆 {current_player.name} WON THE GAME! 🏆")
            return True

        self.players.append(current_player)
        return False


if __name__ == "__main__":
    # Setup Board with Snakes & Ladders
    game_board = Board(size=30)  # Quick 30-cell board for demo
    game_board.add_ladder(3, 15)
    game_board.add_ladder(8, 22)
    game_board.add_snake(17, 4)
    game_board.add_snake(28, 9)

    dice = Dice()
    game = SnakeAndLadderGame(game_board, dice, ["Alice", "Bob"])

    print("=== Starting Snake & Ladder Match ===")
    turn = 1
    while not game.winner and turn <= 50:
        game.play_turn()
        turn += 1
