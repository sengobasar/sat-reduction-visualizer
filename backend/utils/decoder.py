def decode_nqueens(model, metadata):
    """
    Converts a SAT solver model into an N-Queens board representation.
    
    :param model: List of integers (literals) from the SAT solver.
    :param metadata: Dictionary containing 'n' and 'variable_mapping'.
    :return: A 2D list representing the board (1 for queen, 0 for empty).
    """
    if model is None:
        return None

    n = metadata["n"]
    mapping = metadata["variable_mapping"]
    
    # Create empty n x n board
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    for lit in model:
        if lit > 0:
            # If the literal is positive, it means a queen is placed here
            if lit in mapping:
                i, j = mapping[lit]
                board[i][j] = 1
                
    return board
