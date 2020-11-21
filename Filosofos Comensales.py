import threading as thr
from random import random,randint
from time import sleep
filosofosEstado = ['filosofar','filosofar','filosofar','filosofar','filosofar']
tenedor = [thr.RLock(),thr.RLock(),thr.RLock(),thr.RLock(),thr.RLock()]

class Filosofo(thr.Thread):
    def run(self):
        while True:
            filósofo = randint(0,4)
            if filosofosEstado[filósofo] == 'filosofar':
                filosofosEstado[filósofo] = 'esperando'
            elif filosofosEstado[filósofo] == 'esperando':
                tenedor[filósofo].acquire()
                tenedor[(filósofo+1)%5].acquire()
                filosofosEstado[filósofo] = 'comiendo'
                sleep(randint(0,2))
        
            elif  filosofosEstado[filósofo] == 'comiendo':
                if randint(0,10)%2 == 0:
                    filosofosEstado[filósofo] = 'esperando'
                    tenedor[filósofo].release()
                    tenedor[(filósofo+1)%5].release()
                else:
                    filosofosEstado[filósofo] = 'filosofar'
            print(f"{filosofosEstado=}")        
        
# principal
f = [Filosofo(),Filosofo(),Filosofo(),Filosofo(),Filosofo()]
for i in range(5):
    f[i].start()

