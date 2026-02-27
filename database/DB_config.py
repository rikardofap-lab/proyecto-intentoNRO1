import pymysql

class DBConfig:

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "bd_intento_nro1"

    def conectar(self):
        self.con = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.con.cursor()

    def desconectar(self):
        try:
            if self.con.open:
                self.con.close()
        except:
            pass
