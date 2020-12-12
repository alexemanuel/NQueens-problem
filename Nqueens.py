class NQueens():

    """The problem of placing N queens on an NxN board with none attacking
    each other.  A state is represented as an N-element array, where
    a value of r in the c-th entry means there is a queen at column c,
    row r, and a value of None means that the c-th column has not been
    filled in yet.  We fill in columns left to right.
    """

    def __init__(self, N):
        self.N = N
        self.initial = [None] * N

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
        if state[-1] is not None:
            return []  # All columns filled; no successors
        else:
            col = state.index(None)
            return [row for row in range(self.N)
                    if not self._conflicted(state, row, col)]

    def result(self, state, row):
        """Place the next queen at the given row."""
        col = state.index(None)
        new = state[:]
        new[col] = row
        return new

    def _conflicted(self, state, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self._conflict(row, col, state[c], c)
                   for c in range(col))

    def _conflict(self, row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)   # same / diagonal

    def goal_test(self, state):
        """Check if all columns filled, no conflicts."""
        if state[-1] is None:
            return False
        return not any(self._conflicted(state, state[col], col)
                       for col in range(len(state)))


