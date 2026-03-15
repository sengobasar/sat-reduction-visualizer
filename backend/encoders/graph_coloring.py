from backend.models.cnf_formula import CNFFormula

def var(v, c, k):
    """
    Maps vertex v and color c to a unique variable index.
    v is vertex index (0-indexed), c is color index (0-indexed).
    """
    return v * k + c + 1

class GraphColoringEncoder:
    """
    Converts the Graph Coloring problem into a CNF formula.
    """

    def __init__(self, graph, k):
        """
        :param graph: Adjacency list {v: [neighbors]}
        :param k: Number of colors
        """
        self.graph = graph
        self.k = k
        self.formula = CNFFormula()

    def encode(self):
        """
        Generates the CNF formula for the Graph Coloring problem.
        Returns the CNFFormula object and mapping metadata.
        """
        nodes = list(self.graph.keys())
        k = self.k

        # 1. Each vertex must have at least one color
        for v in nodes:
            clause = [var(v, c, k) for c in range(k)]
            self.formula.add_clause(clause)

        # 2. A vertex cannot have two colors
        for v in nodes:
            for c1 in range(k):
                for c2 in range(c1 + 1, k):
                    self.formula.add_clause([-var(v, c1, k), -var(v, c2, k)])

        # 3. Adjacent vertices cannot share a color
        for u in nodes:
            for v in self.graph[u]:
                if u < v:  # Avoid adding the same constraint twice for undirected edges
                    for c in range(k):
                        self.formula.add_clause([-var(u, c, k), -var(v, c, k)])

        metadata = {
            "graph": self.graph,
            "k": k,
            "variable_mapping": {var(v, c, k): (v, c) for v in nodes for c in range(k)}
        }

        return self.formula, metadata
