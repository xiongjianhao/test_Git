import multiprocessing

class Worker:
    def run(self, msg):
        print '%s, it works!' % msg

def wrap(worker, msg):
    worker.run(msg)

def start_process():
    print 'Starting',multiprocessing.current_process().name

if __name__=='__main__':
    pool = multiprocessing.Pool(processes=2, initializer=start_process,)
    pool.apply_async(wrap, args=(Worker(), 'congbo'))
    pool.close()
    pool.join()
