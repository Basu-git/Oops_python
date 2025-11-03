#3. Create methods to start and stop a `Machine` class and call them.
class Machine:
    def __init__(self):
        pass
    def start(self):
        print("The machine is starting")
    def stop(self):
        print("The machine is stopped")
    def restart(self):
        print("The machine is restarted")
m=Machine()
m.start()
m.restart()
m.stop()