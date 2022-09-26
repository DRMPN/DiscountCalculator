import datetime
import math


class DynamicDeposit:
    def __init__(self, d1, s, maxs, i=6, op=3):
        """"
        d1: Дата завершения выполнения заказа
        s:  Сумма желаемой выплаты
        maxs: максимальная сумма по которой заказчик может произвести раннюю выплату
        i: годовая ставка по вкладу
        op: Операционные издержки
        """
        self.d2 = 60
        self.d1 = datetime.date(int(d1[0]), int(d1[1]), int(d1[2]))
        self.s = int(s)
        self.op = op
        self.i = i
        self.maxs = maxs

        self.DMAX = 12

    def __getdmin(self, t):
        return ((self.maxs * pow(1 + (self.i / 100) / 365, self.d2 - t) - self.maxs) * 100) \
               / self.s + self.op

    def calc(self, t):
        """"
        t: дата ранней выплаты
        """

        t = [int(i) for i in t.split('-')]
        t = datetime.date(t[0], t[1], t[2])

        t = int((t - self.d1).days)
        dmin = self.__getdmin(t)
        dmax = self.DMAX
        a = 0.02
        c = 0

        l = ((1 + math.exp(a*t + c))*dmin - dmax)/math.exp(a*t +c)
        k = (dmax - l)*2

        eq = round(k / (1 + math.exp(a * t + c)) + l,2)

        if eq > 12:
            return 12
        elif eq < 3:
            return 3
        else:
            return eq

        


#if __name__ == '__main__':
#    dd = DynamicDeposit(datetime.date(2022, 5, 22), 1000000, 5000000)
#    print(dd.calc(datetime.date(2022, 4, 22)))
