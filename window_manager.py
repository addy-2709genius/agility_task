from collections import OrderedDict
 
 
class WindowManager:
    def __init__(self):
        self.state = {}
        self.zOrder = OrderedDict()
 
    def open(self, id):
        if id in self.zOrder:
            self.zOrder.move_to_end(id)
        else:
            self.zOrder[id] = None
        self.state[id] = "OPEN"
 
    def focus(self, id):
        if id not in self.state:
            return
        if id in self.zOrder:
            self.zOrder.move_to_end(id)
        else:
            self.zOrder[id] = None
        self.state[id] = "OPEN"
 
    def minimize(self, id):
        if self.state.get(id) != "OPEN":
            return
        del self.zOrder[id]
        self.state[id] = "MINIMIZED"
 
    def restore(self, id):
        if self.state.get(id) != "MINIMIZED":
            return
        self.zOrder[id] = None
        self.state[id] = "OPEN"
 
    def close(self, id):
        if id not in self.state:
            return
        if self.state[id] == "OPEN":
            del self.zOrder[id]
        del self.state[id]
 
    def top(self):
        if not self.zOrder:
            return -1
        return next(reversed(self.zOrder))
 
    def list(self):
        return list(reversed(self.zOrder))
 
 
if __name__ == "__main__":
    wm = WindowManager()
    wm.open(10)
    wm.open(20)
    wm.open(30)
    print(wm.list())
    wm.minimize(20)
    print(wm.top())
    wm.focus(20)
    print(wm.list())
    wm.close(10)
    print(wm.top())
 
