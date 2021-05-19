from .searchWorker import SearchWorker
from time import sleep


class LoopSearchWorker(object):
    def worker(self, allProcs: [SearchWorker]):
        while True:
            for proc in allProcs:
                proc.resume() 
                sleep(15) ## TODO changer le timing
                proc.pause()
                sleep(1)

