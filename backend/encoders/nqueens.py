from backend.models.cnf_formula import CNFFormula

def var(i, j, n):
    """
    Maps board coordinates (i, j) to a unique variable index.
    i, j are 0-indexed.
    """
    return i * n + j + 1

class NQueensEncoder:
    """
    Converts the N-Queens problem into a CNF formula.
    """

    def __init__(self, n):
        self.n = n
        self.formula = CNFFormula()

    def encode(self):
        """
        Generates the CNF formula for the N-Queens problem.
        Returns the CNFFormula object and mapping metadata.
        """
        n = self.n
        
        # 1. Each row must contain at least one queen
        for i in range(n):
            clause = [var(i, j, n) for j in range(n)]
            self.formula.add_clause(clause)

        # 2. A row cannot contain two queens
        for i in range(n):
            for j in range(n):
                for k in range(j + 1, n):
                    self.formula.add_clause([-var(i, j, n), -var(i, k, n)])

        # 3. A column cannot contain two queens
        for j in range(n):
            for i in range(n):
                for k in range(i + 1, n):
                    self.formula.add_clause([-var(i, j, n), -var(k, j, n)])

        # 4. Diagonal constraints
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        if (i, j) == (k, l):
                            continue
                        if abs(i - k) == abs(j - l):
                            # To avoid adding the same symmetry twice (i,j) < (k,l)
                            if (i * n + j) < (k * n + l):
                                self.formula.add_clause([-var(i, j, n), -var(k, l, n)])

        metadata = {
            "n": n,
            "variable_mapping": {var(i, j, n): (i, j) for i in range(n) for j in range(n)}
        }
        
        return self.formula, metadata
