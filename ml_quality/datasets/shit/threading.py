import threading

class messenger(threading.Thread):
    def run(self)
    for _ in range(10):
        print(threading.currentThread().getName())

        x = messenger(name = "send out messages")
        y = messenger(name = "recieve messages")

        x.start()
        y.start()
