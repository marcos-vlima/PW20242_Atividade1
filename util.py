import sqlite3
import os
from sql.produto_sql import *

_banco = "dados.db"

def obter_conexao():
    conexao = sqlite3.connect(_banco)
    conexao.autocommit = True
    return conexao

def verificar_banco(banco = _banco):
    if not os.path.exists(banco):
        inicializar_banco()

def inicializar_banco():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(SQL_CRIAR_TABELA)
    cursor.execute(SQL_INSERIR, ("Bicicleta","Bicicross",5,850.99,"Bicicletas"))
    cursor.execute(SQL_INSERIR, ("Stake","Profissional",3,1199.99,"Skates"))
    cursor.execute(SQL_INSERIR, ("Bicicleta Infantil","Caloi",6,299.99,"Bicicletas"))
    conexao.close()


