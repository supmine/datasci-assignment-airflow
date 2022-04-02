import uvicorn
from fastapi import FastAPI

from pydantic import BaseModel


class Equation(BaseModel):
    m: float
    x: float
    c: float


app = FastAPI()


@app.post("/compute/")
async def compute_linear(equation: Equation):
    return {"y": equation.m * equation.x + equation.c}


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
