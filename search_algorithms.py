from utils import timer


@timer
def breadth_first_search(n_queens):
    """ BFS (breadth_first_search) implementation.
        n_queens = instance of NQueens class
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

        next_actions = n_queens.actions(current_state)

        for next_action in next_actions:
            all_states.append(n_queens.result(current_state, next_action))

    return initial_state


@timer
def depth_first_search(n_queens):
    """ DFS (depth_first_search) implementation.
        n_queens = instance of NQueens class 
        returns: a list of states, each index in list is equivalent to a column
                and its value is equivalent to the row. ex: states[2]=4 means 
                that there is a queen at position (col=2, row=4). OBS: It is 0-indexed
    """

    def dfs(current_state):
        next_actions = n_queens.actions(current_state)

        for next_action in next_actions:
            next_state = n_queens.result(current_state, next_action)
            final_state = dfs(next_state) 

            if n_queens.goal_test(final_state):
                return final_state

        return current_state 


    initial_state = n_queens.initial
    final_state = dfs(initial_state)

    return final_state
    
    
    
    

