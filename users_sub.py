from time import time
from count import *

class User:
    def __init__(self, user_data: tuple):
        self.id = user_data[0]
        self.user_id = user_data[1]
        self.name = user_data[2]
        self.ref = user_data[3]
        self.sub = user_data[4]
        self.balance = user_data[5]


    def __repr__(self):
        return "<(User(id: %s, user_id: %s, user_name: %s ))>" % (self.user_id, self.id, self.name)


    @staticmethod
    def __calc_price(days: int) -> int:
        if days < 1:
            raise Exception('invalid')
        elif days < 7:
            return days * 20
        elif days < 14:
            return days * 18
        elif days < 30:
            return days * 15
        else:
            return days * 10


    def check_sub(self):
        """Возращает True когда подписка не истекла"""
        return time() < self.sub


    def update_sub(self, upd_time: int):
        '''Добавляем время подписки'''
        if self.check_sub():
            self.sub += upd_time
        else:
            self.sub = int(time()) + upd_time


    def buy_sub(self, days):
        """Вернёт False если денег нет ,Вернёт True если деньги есть"""
        price = self.__calc_price(days)
        if price <= self.balance:
            self.balance -= price
            self.update_sub(days * 24 * 60 * 60)
            return True
        return False

    def dict(self):
        return __dict__


    def get_sub_time(self):
        if not self.check_sub():
            return 'Ваша подписка закончилась'
        s_time = self.sub - int(time())
        d = s_time // (3600 * 24)
        h = (s_time -(d * 3600 * 24)) // 3600
        if  s_time > 24 * 3600:
            return f'Осталось {d} {count_text(d,["день", "дня", "дней"])} {h} {count_text(h,["час", "часа", "часов"])}'
        return f'Осталось {d} {count_text(d, ["день", "дня", "дней"])}    {h} {count_text(h, ["час", "часа", "часов"])}'


