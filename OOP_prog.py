'''
Мой счет
'''
class Bill:
    def __init__(self):
        self.money = 0
    def add(self, count):
        '''
        Добавление денег на счет
        :param count:
        :return:
        '''
        self.money += count
    def buy(self, count, name):
        '''
        Покука
        :param count:
        :param name:
        :return:
        '''
        pass

if __name__ == 'main':
    leo_bill = Bill()
    print(leo_bill.money)

    leo_bill.add(10)
    leo_bill.add(10)

    print(leo_bill.money)

    kate_bill = Bill()
    print(kate_bill.money)

    kate_bill.add(1)
    print(kate_bill.money)

    print('А у Лео осталось 30 т.к. это другой обьект', leo_bill.money)