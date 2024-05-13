import json

class ReadJson():
    def __init__(self, path) -> None:
        self.path = path

    def getData(self,field):
        ptr = open(self.path)
        data = json.loads(ptr.read())
        return data[field]
