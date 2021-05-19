from .searchWorker import SearchWorker
import multiprocessing
import psutil


class SearchProcess(object):
    """process class to create a single process for a keyword"""
    def __init__(self, mysearch, pipe):
        self.pipe = pipe
        self.searchWorker = SearchWorker(mysearch)

    def run(self):
        """run process"""
        self.process = multiprocessing.Process(target=self.searchWorker.worker, args=[self.pipe])
        self.process.start()
        self.p = psutil.Process(self.process.pid)

    def pause(self):
        """pause process"""
        self.p.suspend()

    def resume(self):
        """resume process"""
        self.p.resume()

    def terminate(self):
        """terminate process"""
        self.p.resume()
        self.process.terminate()
        self.process.join()
