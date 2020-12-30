from datetime import date as Date
from datetime import datetime
from datetime import timedelta

def date_from_string(date):
    date_template = '%d.%m.%Y'
    return datetime.strptime(date, date_template).date()


class Calculator():
    def __init__(self, limit):
        self.records = []
        self.limit = limit

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):
        today = Date.today()
        spent_today = 0
        for record in self.records:
            if today == record.date:
                spent_today += record.amount
        return spent_today

    def get_week_stats(self):
        today = Date.today()
        spent_week = 0
        for record in self.records:
            if today - record.date <= timedelta(days = 7):
                spent_week += record.amount
        return spent_week

    def get_today_remained(self):
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    def get_calories_remained(slef):
        ans = super().get_today_remained()
        if ans > 0:
            return 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более %d кКал'%(ans)
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    EURO_RATE = 70.0
    USD_RATE = 65.0

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        ans = super().get_today_remained()
        if currency == 'rub':
            course = 1
            valuta = 'руб'
        elif currency == 'usd':
            valuta = 'USD'
            course = self.USD_RATE
        else:
            valuta = 'Euro'
            course = self.EURO_RATE

        if round(ans/course) == ans/course:
            res = '%.1f'%(abs(ans/course))
        else:
            res = '%.2f'%(abs(ans/course))

        if ans > 0:
            return 'На сегодня осталось %s %s'%(res, valuta)
        elif ans == 0:
            return 'Денег нет, держись'
        else:
            return 'Денег нет, держись: твой долг - %s %s'%(res, valuta)

class Record():
    def __init__(self, amount = 0, comment = '', date = Date.today().strftime('%d.%m.%Y') ):
        self.amount = amount
        self.comment = comment
        self.date = date_from_string(date)
