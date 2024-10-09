from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import uvicorn

from models.produto_model import Produto
from repositories.produto_repo import inserir_produto
from util import verificar_banco

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="./static"), name="static")

@app.get("/")
def exibir_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.get("/cadastro_recebido")
def get_cadastro_recebido(request: Request, produto: Produto):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request, "produto": produto})

@app.post("/post_cadastro")
def post_cadastro(
    request: Request, 
    nome: str = Form(...), 
    descricao: str = Form(...), 
    estoque: int = Form(...), 
    preco: str = Form(...),
    categoria: str = Form(...)):
    preco = float(preco.replace(',', '.'))
    preco = round(preco,2)
    produto = Produto(None, nome, descricao, estoque, preco, categoria)
    produto = inserir_produto(produto)
    if (produto):
        return templates.TemplateResponse("cadastro_recebido.html", {"request": request, "produto": produto})
    else:
        return templates.TemplateResponse("cadastro.html", {"request": request})
        
if __name__ == "__main__":
    verificar_banco()

    uvicorn.run("main:app", port=8787, reload=True)
