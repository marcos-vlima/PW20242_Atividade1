from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="./static"), name="static")

@app.get("/")
def exibir_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
def get_contato(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_cadastro")
def post_contato(
    request: Request, 
    nome: str = Form(...), 
    descricao: str = Form(...), 
    estoque: int = Form(...), 
    preco: int = Form(...),
    categoria: int = Form(...)):
    return RedirectResponse("/", 303)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8787, reload=True)
