import sys

from Nqueens import NQueens
from search_algorithms import breadth_first_search as BFS
from utils import print_queens_board_positions


if __name__ == '__main__':
    #Number of queens and board size (NxN)
    N = int(sys.argv[1])
    n_queens = NQueens(N)

    queens_positions = BFS(n_queens)

    if n_queens.goal_test(queens_positions):
        print(f"One solution was found: {queens_positions}")
        print_queens_board_positions(queens_positions)

    else:
        print("Could not solve the problem")
        

