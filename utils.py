import functools
from string import ascii_lowercase as board_columns
import time


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.time()
        output = func(*args, **kwargs)
        end_time = time.time()

        print(f"Elapsed Time: {end_time - start_time:.4f}s")
        return output

    return wrapper


def print_queens_board_positions(queens_positions):
    """Print queens positions on the board"""

    print("Queens positions on the board:")

    for i in range(len(queens_positions)):
        print(f"{i + 1}° Queen: {board_columns[i]}{queens_positions[i] + 1}")


#TODO
def build_board(queens_positions):
    """Print the chess board with all queens"""


