from .loopSearchWorker import LoopSearchWorker
from .searchProcess import SearchProcess
import multiprocessing
import psutil


class LoopSearch(object):
    def __init__(self, pipe, keywords):
        self.pipe = pipe
        self.loopSearchWorker = LoopSearchWorker()
        self.allProcs = [SearchProcess(keyword, self.pipe) for keyword in keywords]
        for proc in self.allProcs:
            proc.run()
            proc.pause()

    def run(self):
        self.process = multiprocessing.Process(target=self.loopSearchWorker.worker, args=[self.allProcs])
        self.process.start()
        self.p = psutil.Process(self.process.pid)

    def terminateAllProcs(self):
        for proc in self.allProcs:
            proc.resume()
            proc.process.terminate()
            proc.process.join()
        self.p.resume()
        self.process.terminate()
        self.process.join()

    def pause(self):
        self.p.suspend()
        [proc.pause() for proc in self.allProcs]

    def resume(self):
        self.p.resume()
