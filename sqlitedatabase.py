import sys
from PySide2.QtSql import (QSqlDatabase, QSqlQuery, QSqlQueryModel)

class SqliteDatabase():
''' Helper methods for sqlite. '''

    def __init__(self, db_type=':memory:'):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(db_type)
        
        if not self.db.open():
            print("Could not open database:", db_type)
            sys.exit(1)

    def check_error(self, q, db):
        ler = q.lastError()
        if ler.isValid():
            self.db.close()
            print('Yorgi:', ler.text())
            sys.exit(1)

    def select(self, statement):
        #print(statement)
        q = QSqlQuery()
        if not q.exec_(statement):
            self.check_error(q, self.db)
        return q

    def getConnection(self):
        return self.db
