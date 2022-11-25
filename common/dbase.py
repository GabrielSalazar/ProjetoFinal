#import mysql.connector

''''
class Dbase:
    def __init__(self):
        self.__sql_script = None
        self.__conn= None

    @property
    def sql_script(self):
        return self.__sql_script


    def __connect(self):
        try:
            self.__conn = mysql.connector.connect(
                host="localhost",
                user="finance",
                password="blog1001"
            )
        except Exception as e:
            print(e)


    def create(self, insert_shell, insert_data):
        try:
            self.__connect()
            cursor = self.__conn.cursor()
            cursor.execute(insert_shell, insert_data)

            self.__conn.commit()
            self.__conn.close()
            return True

        except Exception as e:
            print(e)
            raise
            return False
        finally:
            if self.__conn.is_connected():
                cursor.close()
                self.__conn.close()


    def read(self, select_shell, select_data):
        try:
            self.__connect()
            cursor = self.__conn.cursor()
            cursor.execute(select_shell, select_data)

            return cursor.fetchall()

        except Exception as e:
            print(e)
            raise
            return None
        finally:
            if self.__conn.is_connected():
                cursor.close()
                self.__conn.close()


    def update(self, insert_shell, insert_data):
        try:
            self.__connect()
            cursor = self.__conn.cursor()
            cursor.execute(insert_shell, insert_data)

            self.__conn.commit()
            self.__conn.close()
            return True

        except Exception as e:
            print(e)
            raise
            return False
        finally:
            if self.__conn.is_connected():
                cursor.close()
                self.__conn.close()
                print("MySQL connection is closed")


    def delete(self, insert_shell, insert_data):
        try:
            self.__connect()
            cursor = self.__conn.cursor()
            cursor.execute(insert_shell, insert_data)

            self.__conn.commit()
            self.__conn.close()
            return True

        except Exception as e:
            print(e)
            raise
            return False
        finally:
            if self.__conn.is_connected():
                cursor.close()
                self.__conn.close()
                print("MySQL connection is closed")
'''
