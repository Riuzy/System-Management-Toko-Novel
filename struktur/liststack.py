import json
from struktur.struct import Novel

class Stack_Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Novel_Stack:
    def __init__(self):
        self.file_path = "data/novel_data.json"
        self.top = None

    def push_novel(self, novel):
        new_node = Stack_Node(novel)
        new_node.next = self.top
        self.top = new_node

        try:
            with open(self.file_path, "r") as file:
                novels = json.load(file)
        except FileNotFoundError:
            novels = []
        found = False
        existing_novel_index = None  
        for i in range(len(novels)):
            if novels[i]['judul'].lower() == novel.judul.lower():
                existing_novel_index = i
                found = True
                break

        if found:
            novels[existing_novel_index]['stok'] = novel.stok
        else:
            new_novel = novel.to_dict()
            novels = [new_novel] + novels

        with open(self.file_path, "w") as file:
            json.dump(novels, file, indent=4)

    def display(self):
        """Fetches the data directly from the JSON file."""
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
