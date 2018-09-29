import os
import fnmatch
import json
import random

class Assets():
    __BASE_DIR = os.path.abspath(os.path.dirname(__file__) + "/../")
    
    def __init__(self):
        self._data = {}
        self._map = {}
        self._datapacks = []
        self.load_datapack("astumoleth")
        #fetch datapack data
        #load datapacks
        #fetch global mapping
    
    def load_datapack(self, name):
        if name == "astumoleth":
            dir = self.__BASE_DIR + "/assets"
        else:
            dir = self.__BASE_DIR + "/datapacks/" + name
        self._datapacks += [name]
        self._title_load(dir + "/titles", name)

    def unload_datapack(self, name):
        if not name in self._datapacks:
            return
        if name == "astumoleth":
            return

    def __getitem__(self, id): #global mapping -> data -> object
        if id == "title": #ranomly choose one of the mapped (currently all)
            titles = [title for id, title in self._data.items() if fnmatch.fnmatch(id, "*:titles:*")]
            return titles[random.randint(0,len(titles)-1)]

    def _title_load(self, dir, name):
        files = [file for file in os.listdir(dir) if fnmatch.fnmatch(file, "*.json")]
        for file in files:
            data = json.load(open(dir + "/" + file))
            for id, title in data.items():
                self._data[name + ':titles:' + id] = title
            

if __name__ == "__main__":
    assets = Assets()
    print(assets._data)
