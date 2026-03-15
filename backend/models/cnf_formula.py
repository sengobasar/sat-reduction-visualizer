class CNFFormula:
    """
    Represents a Boolean formula in Conjunctive Normal Form (CNF).
    Variables are represented as positive integers starting from 1.
    Literals are represented as integers, where negative integers represent negated variables.
    """

    def __init__(self):
        self.clauses = []
        self.num_variables = 0

    def add_variable(self):
        """
        Increments the variable count and returns the new variable index.
        """
        self.num_variables += 1
        return self.num_variables

    def add_clause(self, literals):
        """
        Adds a clause to the formula.
        :param literals: A list of integers representing literals.
        """
        self.clauses.append(list(literals))
        # Update num_variables if literals reference indices higher than current count
        for lit in literals:
            self.num_variables = max(self.num_variables, abs(lit))

    def get_clauses(self):
        """
        Returns the list of clauses, suitable for most SAT solvers (e.g., glucose, minisat).
        """
        return self.clauses

    def __str__(self):
        """
        Returns a pretty-printed string representation of the CNF formula.
        """
        if not self.clauses:
            return "True"
        
        clause_strs = []
        for clause in self.clauses:
            lit_strs = []
            for lit in clause:
                if lit > 0:
                    lit_strs.append(f"x{lit}")
                else:
                    lit_strs.append(f"¬x{abs(lit)}")
            clause_strs.append("(" + " ∨ ".join(lit_strs) + ")")
        
        return " ∧ ".join(clause_strs)
