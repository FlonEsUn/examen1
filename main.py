class Head:
    money = 1000
    mind = 78
    health = 87
    harizma = 50
    age = 43


class Worker(Head):
    money = 100
    mind = 91
    health = 87
    age = 21

    def __init__(self):
        self.age += 5
        self.mind -= 10

    def allmethods(self):
        print(f'Worker mind = {worker.mind}')
        print(f'Worker health = {worker.health}')
        print(f'Worker age = {worker.age}')
        print(f'Worker harizma = {worker.harizma}')
        print(f'Worker money = {worker.money}')


head = Head()
worker = Worker()
worker.allmethods()
