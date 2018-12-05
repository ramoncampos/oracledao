# coding=utf8

# module oracle-dao.py
# modulo criado para separar a camada de conexao a banco de dados Oracle
# e prover interface para métodos basicos de DML, Select e chamada a procedures/funcoes
# Pre-requisito - cx_Oracle
# Usado com Python 3

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
]

__title__ = "oracle-dao"
__summary__ = ("""oradbdao e um modulo que prove conexao com Oracle Database através do cx-Oracle, e encapsula metodos simples""")
__uri__ = "http://#"

__version_info__ = (0, 1, 1)
__version__ = '.'.join(map(str, __version_info__))

__author__ = "Joel Santos / Ramon Campos"
__email__ = "r7campos@gmail.com"

__license__ = "GNU Lesser General Public License (LGPL)"
__copyright__ = "Copyright 2017-2018 {0}".format(__author__)


import cx_Oracle

class ora_db(object):
    _dbConn = None
    _cursor = None

    def __init__(self, _objetoDB):

        # Carregando dados de configuração
        user = _objetoDB['user']
        passwd = _objetoDB['passwd']
        tns_connect = _objetoDB['tns_connect']

        try:
            self._dbConn = cx_Oracle.Connection(user, passwd, tns_connect, encoding='UTF-8', nencoding='UTF-8')

            self._cursor = self._dbConn.cursor()

        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 1017:
                print('Please check your credentials.')
            else:
                print('Database connection error: %s'.format(e))
            raise

    def execProc(self, _procName, _parameters):
        self._cursor.callproc(_procName, _parameters)

    def execCommandParam(self, _query, _params):
        self._cursor.prepare(_query)
        self._cursor.execute(None, _params)

    def execCommandParamReturn(self, _query, _params):
        self._cursor.prepare(_query)
        self._cursor.execute(None, _params)
        data = self._cursor.fetchall()
        return data

    def execCommand(self, _query):
        self._cursor.execute(_query)

    def execCommandReturn(self, _query):
        self._cursor.execute(_query)
        data = self._cursor.fetchall()
        return data

    def execCommit(self):
        self._dbConn.commit()

    def connClose(self):
        self._dbConn.close()

    def __del__(self):
        self._dbConn.commit()
        self._dbConn.close()
