import sqlite3
from time import time


class UsersCRUD:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.conn.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INT NOT NULL,
        user_name VARCHAR(24) NOT NULL,
        user_ref VARCHAR(16) NOT NULL,
        sub INT NOT NULL,
        balance INT NOT NULL DEFAULT 0);""")
        self.cursor = self.conn.cursor()

    def __create_user(self, user_id, user_name, user_ref=0, sub_time=0):
        sub_time += int(time())
        self.cursor.execute("""INSERT INTO users(user_id, user_name,user_ref, sub) VALUES(?,?,?,?)""",
                            (user_id, user_name, user_ref, sub_time))
        self.conn.commit()

    def __exist_user(self, user_id) -> None:
        user = self.cursor.execute("""SELECT * FROM users WHERE user_id=?""", (user_id,)).fetchone()
        return bool(user)

    def add_new_user(self, user_id, user_name, user_ref=0, sub_time=0) -> bool:
        """Добавляет нового пользователя если его нет если пользователь есть то возвращает TRUE если нет то FALSE"""
        if self.__exist_user(user_id):
            return False
        if not (user_ref and self.__exist_user(user_ref)):
            user_ref = 0
        self.__create_user(user_id, user_name, user_ref, sub_time)
        return True

    def get_count_ref(self, user_id):
        # return len(self.cursor.execute("""SELECT * FROM users WHERE user_ref=?""", (168327008,)).fetchall())
        count = self.cursor.execute("""SELECT COUNT(user_id) FROM users WHERE user_ref=?""", (user_id,)).fetchone()
        return count[0]

    def get_percent_of_paymounts_ref(self, paymount, user_id):
        user_id_ref = self.cursor.execute("""SELECT user_ref FROM users WHERE user_id=?""", (user_id,)).fetchone()
        self.cursor.execute(f"UPDATE users SET balance = balance + {paymount} WHERE user_id ={user_id}")
        if user_id_ref[0]:
            balance = int(int(paymount) * 0.1)
            self.cursor.execute(f"UPDATE users SET balance = balance + {balance} WHERE user_id ={1683270028}")
        self.conn.commit()

    def get_ballance(self,user_id):
        balance = self.cursor.execute("""SELECT balance FROM users WHERE user_id=?""", (user_id,)).fetchone()
        return balance[0]

    def close_conn(self):
        self.conn.close()
        print('Соединение закрыто')