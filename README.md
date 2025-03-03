# Projeto Oracle-dao

Oracle-dao é um módulo que nasceu da necessidade de facilitar o uso do modulo cx-oracle. Dessa forma, ele é para ser usado para conectar bases de dados Oracle.
Este módulo provê interface para métodos basicos de DML, Select e chamada a Procedures/Funções. Além disso foi implantado um retorno no formato dicionário, facilitando muito o acesso ao ddo a partir do nome do campo.
Pre-requisito: cx_Oracle
Compatível com Python 3.

## Changelog
- 0.1.1 - Incluído nos parâmetros de conexão o enconding UTF-8
- 0.1.2 - Incluído método para retornar linhas como dicionario

## Exemplos de uso

1. Conectando à base de dados
from oracledao import ora_db

db_source = {
    'user':'usuario',
    'passwd':'senha',
    'tns_connect':"""(DESCRIPTION= (ADDRESS= (PROTOCOL=TCP) (HOST = exscegt-scan.b2w) (PORT = 1521))
                                    (CONNECT_DATA= (SERVER = DEDICATED)(SERVICE_NAME= BWSCEPR)))"""
    }

db = ora_db(db_source)

2. Consultando com parametros e retornando dicionario

query = 'query com parametro como :dt_recebido'
params = {}
params['dt_recebido'] = self.dt_recebido
params['origem'] = self.origem

db.execCommandParamReturnAsDict(query, params)
