import json
from os.path import isfile


class JsonDB(dict):
    """
    create a dictionary object with store and load methods to a certain path
    """
    def __init__(self, path: str):
        self.path = path
        if isfile(self.path):
            self.load()
        else:
            super().__init__()

    def load(self):
        with open(self.path, 'rb') as file:
            super().__init__(json.load(file))

    def store(self):
        if self:
            if isfile(self.path):
                self.load()
            with open(self.path, 'w') as file:
                jsn = json.dumps(self, indent=2)
                file.write(jsn)


if __name__ == "__main__":
    tst_fn = "d:/tmp/test.json"
    from os import remove
    remove(tst_fn)
    tst = JsonDB(tst_fn)
    tst2 = JsonDB(tst_fn)
    tst2['a'] = 1
    tst2.load()
    tst2.store()
    tst['b'] = 2
    tst.store()
    print(JsonDB(tst_fn))
