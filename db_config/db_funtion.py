import pymysql


def conn_db(db_host,
            db_port,
            db_user,
            db_name,
            db_password):
    try:
        return pymysql.connect(db=db_name,
                               host=db_host,
                               port=db_port,
                               user=db_user,
                               password=db_password)

    except Exception as e:
        print(f"Error connecting to MariaDB Platform: {e}")


class db_execute:
    def __init__(self,
                 db_host,
                 db_port,
                 db_user,
                 db_dbname,
                 db_password):
        try:
            self.conn = conn_db(db_host, db_port, db_user, db_dbname, db_password)
            self.curs = self.conn.cursor()
        except AttributeError as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            raise

    def execute_insert(self, sql, value=None) -> (bool, int):
        try:
            if value:
                self.curs.execute(sql, value)
            else:
                self.curs.execute(sql)
            rowid = str(self.curs.lastrowid)
            self.conn.commit()
            return rowid

        except Exception as e:
            print(e)
            raise

    def execute_select(self, sql: str):
        try:
            self.curs.execute(sql)
            return self.curs.fetchall()

        except Exception as e:
            print(e)
            raise

    def execute_update(self, sql: str):
        try:
            self.curs.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            raise

    def execute_delete(self, sql: str):
        try:
            self.curs.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            raise