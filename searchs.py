def breadth_first_search (n_queens):
    """ BFS (breadth_first_search) implementation.
        n_queens = number of queens in a chess board
        returns: a list of states, each index in list is equivalent to a column
                and its value is equivalent to the row. ex: states[2]=4 means 
                that there is a queen at position (col=2, row=4). OBS: It is 0-indexed
    """

    initial_state = n_queens.initial
    all_states = [initial_state]

    while len(all_states) > 0:
        current_state = all_states.pop(0)

        if n_queens.goal_test(current_state):
            return current_state

        possible_next_states = n_queens.actions(current_state)

        for possible_next_state in possible_next_states:
            all_states.append(n_queens.result(current_state, possible_next_state))

    return initial_state
