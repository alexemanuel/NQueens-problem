import argparse 

from Nqueens import NQueens
from search_algorithms import breadth_first_search as BFS
from search_algorithms import depth_first_search as DFS
from utils import print_queens_board_positions


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = "Apply a search algorithm to solve the eight queens problem")

    parser.add_argument("--search_algorithm",
                        help = "Choose between the search algorithms: BFS (breadth_first_search) and DFS (depth_first_search) (default: DFS)",
                        default = "DFS",
                        choices = ["DFS", "BFS"])

    parser.add_argument("--queens_number",
                        help = "Number of queens on the board (default: 8)",
                        type = int,
                        default = 8)

    args = parser.parse_args()

    print(f"Search Algorithm: {args.search_algorithm}")
    print(f"Number of queens on the board: {args.queens_number}")
    print("-------------")

    if args.search_algorithm == "DFS":
        search_algorithm = DFS
    else:
        search_algorithm = BFS

    n_queens = NQueens(args.queens_number)
    queens_positions = search_algorithm(n_queens)

    if n_queens.goal_test(queens_positions):
        print(f"One solution was found: {queens_positions}")
        print("-------------")
        print_queens_board_positions(queens_positions)

    else:
        print("None solution was found")
        

