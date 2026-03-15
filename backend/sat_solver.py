from pysat.solvers import Glucose3

class SATSolver:
    """
    A wrapper around the Glucose3 SAT solver from python-sat.
    """

    def __init__(self, cnf_formula):
        self.cnf_formula = cnf_formula
        self.solver = Glucose3()
        for clause in self.cnf_formula.get_clauses():
            self.solver.add_clause(clause)

    def solve(self):
        """
        Runs the solver. Returns the model (list of literals) if SAT, else None.
        """
        if self.solver.solve():
            return self.solver.get_model()
        return None

def model_to_dict(model):
    """
    Converts a SAT model list into a dictionary mapping variable index to boolean.
    Example: [1, -2, 3] -> {1: True, 2: False, 3: True}
    """
    if model is None:
        return None
    return {abs(lit): lit > 0 for lit in model}
