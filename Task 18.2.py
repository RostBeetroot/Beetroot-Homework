class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def add_worker(self):
        return self.workers

    @add_worker.setter
    def add_worker(self, worker):
        self.workers.append(worker)


class Worker:

    def __init__(self, id_: int, name: str, boss: Boss):
        self.id = id_
        self.name = name
        self.boss = boss
        boss.add_worker = {id_: name}


boss1 = Boss(25, "Jack", "Beetroot")
boss2 = Boss(27, "Oleg", "Orange")
worker1 = Worker(20, "Alex", boss1)
worker2 = Worker(23, "Tom", boss2)
worker3 = Worker(24, "David", boss1)

print(boss1.workers)
print(boss2.workers)
