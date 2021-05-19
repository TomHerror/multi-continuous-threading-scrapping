from threading import Thread


class WriteTh(Thread):
    def __init__(self, pipe):
        Thread.__init__(self)
        self._running = True
        self.pipe = pipe

    def run(self):
        while self._running:
            try:
                print(self.pipe.recv())
            except:
                pass

    def stop(self):
        self._running = False
