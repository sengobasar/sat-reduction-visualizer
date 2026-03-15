from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.main import solve_nqueens, solve_graph_coloring

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NQueensRequest(BaseModel):
    n: int


class GraphColoringRequest(BaseModel):
    graph: dict
    k: int


@app.get("/")
def root():
    return {"message": "SAT Visualizer API running"}


@app.post("/solve/nqueens")
def api_solve_nqueens(req: NQueensRequest):
    return solve_nqueens(req.n)


@app.post("/solve/graph-coloring")
def api_graph_coloring(req: GraphColoringRequest):
    graph = {int(k): v for k, v in req.graph.items()}
    return solve_graph_coloring(graph, req.k)