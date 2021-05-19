from process import LoopSearch, WriteTh 
import PySimpleGUI as sg
import multiprocessing


keywords = [
        "yahoo.fr",
        "hotmail.com",
        "gmail.com"
        ]


class MainView():
    def __init__(self):
        self.layout = [
            [sg.Button("close")],
            [sg.Button("start"), sg.Button("stop")],
            [sg.Output(size=(150, 30))]
        ]
        sg.theme('DarkAmber')
        self.window = sg.Window(
            title="RSSTI", layout=self.layout)
        #
        self.parent_conn, self.child_conn = multiprocessing.Pipe()
        #
        self.mainProcess = LoopSearch(self.child_conn, keywords)
        self.mainProcess.run()
        self.mainProcess.pause()
        #
        self._running = True
        self.printTh = WriteTh(self.parent_conn)
        self.printTh.start()
    
    def read(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'close':
                print('closing \n----------')
                self.mainProcess.terminateAllProcs()
                try:
                    self.child_conn.close()
                    self.parent_conn.close()
                    self.mainProcess.process.terminate()
                    self.mainProcess.process.join()
                    self._running = False
                    self.printTh.stop()
                except:
                    pass
                break
            if event == "start":
                print('start to search \n----------')
                self.mainProcess.resume()
            if event == "stop":
                print('pause the search \n---------')
                self.mainProcess.pause()
