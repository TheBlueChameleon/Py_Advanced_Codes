from multiprocessing import Process, Queue, Value, Lock
import time

def producer (ID, queue, stop, lock) :
    lock.acquire()
    print("producer", ID, "begins production")
    lock.release()
    
    while not stop.value :
        lock.acquire()
        print("producer", ID, "produces goods")
        lock.release()
        
        queue.put(f"stuff from producer #{ID}")
        time.sleep(.1)

def consumer (ID, queue, stop, lock) :
    lock.acquire()
    print("consumer", ID, "begins consumption")
    lock.release()
    
    while not stop.value :
        msg = f"consumer {ID} "
        if queue.empty() :
            msg += "takes a day off."
        else :
            msg += "consumes " + queue.get()
        lock.acquire()
        print(msg)
        lock.release()
        time.sleep(.2)


lock        = Lock()
queue       = Queue()
stop        = Value('b', False)
nProducers  =  5
nConsumers  = 10
worktime    = 5

processes = []
for i in range(nProducers) :
    processes.append(Process(
        target=producer,
        args=(i, queue, stop, lock)
    ))

for i in range(nConsumers) :
    processes.append(Process(
        target=consumer,
        args=(i, queue, stop, lock)
    ))
    
for p in processes : p.start()
time.sleep(worktime)
stop.value = True
for p in processes : p.join()

print("unconsumed goods:", queue.qsize())