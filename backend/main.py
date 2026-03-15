from backend.encoders.nqueens import NQueensEncoder
from backend.sat_solver import SATSolver
from backend.utils.decoder import decode_nqueens

def solve_nqueens(n):
    """
    Runs the full SAT pipeline for the N-Queens problem.
    """
    # 1. & 2. Encode problem
    encoder = NQueensEncoder(n)
    cnf_formula, metadata = encoder.encode()

    # 3. & 4. Solve CNF
    solver = SATSolver(cnf_formula)
    model = solver.solve()

    # 5. Decode results
    board = decode_nqueens(model, metadata)

    return {
        "board": board,
        "clauses": cnf_formula.get_clauses(),
        "num_variables": cnf_formula.num_variables,
        "num_clauses": len(cnf_formula.get_clauses()),
        "metadata": metadata
    }

if __name__ == "__main__":
    # Quick test for N=4
    result = solve_nqueens(4)
    print(f"Solved 4-Queens. Variables: {result['num_variables']}, Clauses: {result['num_clauses']}")
    if result["board"]:
        for row in result["board"]:
            print(row)
    else:
        print("No solution found.")
