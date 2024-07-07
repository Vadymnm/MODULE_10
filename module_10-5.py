import multiprocessing
import time
import datetime
from multiprocessing import Pool

class WarehouseManager():
    def __init__(self):
        super().__init__()
        self.data = data
        self.requests = requests

    def warehouse(self,n):
        for i in range(1, n):
            self.data.update({'product'+str(i): i * 25})
#            print(self.data)
        print('-----------------------------------------------------------------')
        return self.data

    def process_request_(self, requests):
        self.request = requests
        self.data = data
        time.sleep(1)
        print('request=', self.request)
        if self.request[0] in self.data:
            pass
        else:
            print('Добавлениe нового наименования продукта  - ', self.request[0])
            self.data.update({self.request[0]: 0})
        print('текущее сoстояние склада:   ',self.data)
        if self.request[1] == "receipt":
            self.data[self.request[0]] += self.request[2]
        if self.request[1] == "shipment":
            self.data[self.request[0]] -= self.request[2]
        print('результат текущей итерации: ', self.data)
        print('-----------------------------------------------------------------')
        return (self.data)

# +=================================================================================

data = {}

requests = [("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product8", "receipt", 50),
    ("product8", "receipt", 50)]

manager = WarehouseManager()

manager.warehouse(5)       # -  формирование стартового склада
print('Исходное  состояние  склада:', data)


start = datetime.datetime.now()

# =========================================================
print('******************* Class *******************************')

# for request in requests:
#     manager.process_request_(request)
# print('final: ',data)
# print()

# =========================================================
print('******************* Process *******************************')
print()
if __name__ == '__main__':
    with multiprocessing.Pool(processes=1) as pool:
        data_ = pool.map(manager.process_request_, requests)
#        print('pool data_ = ',data_, end='')
        print()
        data = data_[-1]
# # =========================================================

print('final: ',data)
end = datetime.datetime.now()
print(end-start)

