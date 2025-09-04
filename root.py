def hello(name):
    return f"Hi there {name}"

class Root:
    def __init__(self, name):
        self.name=name
    def hello_root(self):
        return f"Hi there {self.name}"