
import random
import time
from threading import Thread

Fig = [1,2,3,4,5,6,7,8,9,10]
lit = ['a','b','c','d','e','f','h','i','j','k']
print('Входной список цифр:',Fig)
print('Входной список букв:',lit)

def printing_list(list):
    for i in range(len(list)):
        _ = 3**(random.randrange(50, 70) * 10000) # имитация работы программы
        time.sleep(1)        # задержка выдачи на печать 1 сек.
        print(list[i])


thread = Thread(target = printing_list,kwargs=dict(list=Fig))
thread.start()

printing_list(lit)

thread.join()