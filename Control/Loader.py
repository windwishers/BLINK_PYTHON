import threading

import DataCenter


class LoadingCsv(threading.Thread):

    def empty(self):
        pass

    def __init__(self, end=empty):
        super(LoadingCsv, self).__init__()
        self.end = end

    def run(self):
        DataCenter.load()
        self.end()
