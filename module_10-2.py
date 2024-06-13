
import random
import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, skill,*args,**kwargs):
        super(Knight,self).__init__(*args,**kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        enemy = 100
        print('Sir ',self.name,' - На нас напали!')
        i = 0
        while enemy > 0:
            _ = 3 ** (random.randrange(50, 70) * 10000)  # имитация работы программы
            i +=1
            enemy -= self.skill
            if enemy < 0:
                enemy = 0
            time.sleep(1)  # задержка выдачи на печать 1 сек.
            print('Sir ',self.name,'сражается',i,'дней, осталось',enemy,'врагов')
            time.sleep(1)  # задержка выдачи на печать 1 сек.
            if enemy <= 0:
                print('Sir ',self.name,'одержал победу спустя',i,'дней')
                print('------------------------------------------------')

vasya = Knight(name='Vasya',skill=20)
print(vasya)
petya = Knight(name='Petya',skill=15)
print(petya)
print('-------------------------------------------')
vasya.start()
petya.start()

vasya.join()
petya.join()

print('Все враги закончились - МЫ  ПОБЕДИЛИ !!!')