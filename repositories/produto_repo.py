from typing import List, Optional
from models.produto_model import Produto
from util import obter_conexao
from sql.produto_sql import *

def obter_cursor():
    with obter_conexao() as conexao:
        return conexao.cursor() 

def criar_tabela():
    cursor = obter_cursor()
    cursor.execute(SQL_CRIAR_TABELA)

def inserir_produto(produto: Produto) -> Optional[Produto]:
    cursor = obter_cursor()
    cursor.execute(SQL_INSERIR, (
        produto.nome, 
        produto.descricao,
        produto.estoque,
        produto.preco,
        produto.categoria
        )
    )

    if cursor.rowcount > 0:
        produto.id = cursor.lastrowid
        return produto
    else:
        return None
        
def atualizar_produto(produto: Produto):
    cursor = obter_cursor()
    cursor.execute(SQL_INSERIR, produto)

def obter_todos_produtos() -> List[Produto]:
    cursor = obter_cursor()
    cursor.execute(SQL_OBTER_TODOS)
    resultado = cursor.fetchall()
    return resultado