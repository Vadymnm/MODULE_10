import random
import threading
import time

tables = {}
is_busy = True

class Table(threading.Thread):
    def __init__(self, number, is_busy):
        super().__init__()
        self.number = number
        self.is_busy = is_busy

    def table_(self, tables):
        tables.update({self.number: self.is_busy})
#        tables = {self.number: self.is_busy}
#        print(tables)
        return tables

# =============================================================

class Cafe(threading.Thread):
    def __init__(self, tables, customer_table, *args, **kwargs):
        super(Cafe, self).__init__(*args, **kwargs)
        self.tables = tables
        self.customer_line = customer_line
        self.customer_table = customer_table

    def customer_arrival(self, n):
#        print(" ===  SELF.CUSTOMER_ARRIVAL  ===")
        self.n = n
        for i in range(self.n):
            _ = 3 ** (random.randint(50, 70) * 10000)
#            time.sleep(2)
            self.customer_line += 1
            self.customer_table.append(self.customer_line)
#        print('Очередь посетителей: ********** ', self.customer_table)
        return self.customer_line

    def serve_customer(self, tables):
        # print(" ===  SELF.SERVE_CUSTOMER  ===")
        # print('serve_customer tables: ', tables, flush=True)
        # print('customer_table: ', customer_table, flush=True)
        # -------  список свободных столиков  -----------
        table_ = []
        for key, value in tables.items():
            if value:
                table_.append(key)
#        print('  ----   свободные столики : ', table_, flush=True)
        print(' -------------------------------------------------------------------------- ')

        while (len(table_) > 0) and (len(self.customer_table) > 0):
            #            _ = 3 ** (random.randint(50, 70) * 10000)
            ind = self.customer_table[0]
            _ = 3 ** (random.randint(50, 70) * 10000)
            print('Шаг (посетитель)  №  ', ind, flush=True)
#            print()
            print('  Необслуженных  посетителей :', self.customer_line, ' pers.;  список:  ', self.customer_table)
            # self.customer_line = cafe.customer_arrival(self.customer_line) # --- пришел новый посетитель ---
            #        print('--- Посетитель №', ind, ' прибыл  ---',flush = True)
#            print(table_)
            print(' Посетитель №', ind, ' сел за стол № ', table_[0], ' и  начал  кушать !', flush=True)
            self.customer_line -= 1                                 # --- очередь уменьшилась на 1 ---
            if len(self.customer_table) > 0:
                self.customer_table.pop(0)
            _ = 3 ** (random.randint(50, 70) * 10000)
            time.sleep(5)                                           # --- посетитель кушает---
            print(' Посетитель №', ind, ' покушал и ушел,  стол № ', table_[0], ' освободился, его нужно прибрать!',
                  flush=True)
            # -- приборка и подготовка столиков для приема посетителей --
            print(' -------------------------------------------------------------------------- ')
        # print('очередь  посетителей: ', self.customer_line)
        # print('свободные столики : ', table_, len(table_))
        # print(tables)
        return self.customer_line


# ****************************************************************************************

customer_line = 0
customer_table = []

print("********************************************")

cafe = Cafe(tables, customer_table)

# ================== СПИСОК ГОЛОДНЫХ  ПОСЕТИТЕЛЕЙ  =======================
print(' ============  Прибыла первая группа посетителей.  ================')
n=7
cust_line = cafe.customer_arrival(n)
print('  +++++  customer_line: ', cust_line, ' pers.', 'customer_table: ', customer_table)

print(' ============  Прибыла новая группа посетителей.  ================')
n=3
cust_line = cafe.customer_arrival(n)
print('  +++++  customer_line: ', cust_line, ' pers.', 'customer_table: ', customer_table)
print(' ============ Посетители  становятся в очередь и ожидают свободный стол')

# ================== СПИСОК  СТОЛИКОВ  КАФЕ  - 3 шт.  =======================
print('=============================================================')
tables = {}
a = Table(1, True)
table1 = a.table_(tables)
tables = {}
a = Table(2, True)
table2 = a.table_(tables)
tables = {}
a = Table(3, True)
table3 = a.table_(tables)
print('Список обслуживаемых столиков', table1, table2, table3)
print('=============================================================')

c1 = threading.Thread(target=cafe.serve_customer, args=(table1,))
c2 = threading.Thread(target=cafe.serve_customer, args=(table2,))
c3 = threading.Thread(target=cafe.serve_customer, args=(table3,))

n=2
print(' ============  А посетители  все  идут !!!.  ================')
while customer_table[-1] < 20:
    cust_line = threading.Thread(target=cafe.customer_arrival(n))
print('  +++++  customer_line: ', cust_line, ' pers.', 'customer_table: ', customer_table)
print(' ============ Посетители  становятся в очередь и ожидают свободный стол')


c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
c3.start()
time.sleep(1)
#cust_line.start()
#time.sleep(1)

# Ожидаем завершения работы обслуживания посетителей
c1.join()
c2.join()
c3.join()
#cust_line.join()
print('    Все посетители обслужены,  столики прибраны,  Больше кушать не хочет никто !!!')
print('    МОЖНО  ЗАКРЫВАТЬСЯ !!!')

