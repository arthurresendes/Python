from fastapi import FastAPI
from pydantic import BaseModel
from banco import selecaoTotal,insercao

app = FastAPI()

class Filme(BaseModel):
    nome: str
    autor: str
    genero: str
    ano: int


@app.get("/verfilmes")
async def filme():
    res = selecaoTotal()
    return res

@app.post("/cadastra")
async def cadastro_filme(filme: Filme):
    novo_filme = {"nome": filme.nome , "autor": filme.autor,"genero": filme.genero, "ano": filme.ano}
    insercao(filme.nome , filme.autor,filme.genero, filme.ano)
    
    return novo_filme


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("apifilmes:app", host="127.0.0.1", port=8000, log_level='info', reload=True)