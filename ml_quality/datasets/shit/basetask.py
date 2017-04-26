import threading

class BaseTask():
    def __init__(self, realtime_db, interval=60):
        self.realtimedb = realtime_db
        self._interval = interval
        self.timer = None

    @property
    def interval(self):
        return self._interval

    @property
    def metrics(self):
        results = self.realtimedb.view('_design/niice_couch/_view/dashboard')
        for r in results :
            yield r.key

    def run(self):
        pass

    def start(self):
        self.timer = threading.Timer(self.interval, self.run)
        self.timer.start()

    def stop(self):
        if self.timer:
            self.timer.cancel()
