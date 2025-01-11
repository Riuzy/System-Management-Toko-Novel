import json
from struktur.struct import Pembeli

class Queue_Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Pembeli_Queue:
    def __init__(self):
        self.file_path = "data/riwayat_pembeli.json"
        self.front = None
        self.rear = None
        self.load_queue()

    def load_queue(self):
        try:
            with open(self.file_path, "r") as file:
                pembeli_data = json.load(file)
                for pembeli in pembeli_data:
                    filtered_pembeli = {key: value for key, value in pembeli.items() if key != "total_harga"}
                    self.enqueue(Pembeli(**filtered_pembeli))
        except FileNotFoundError:
            pass

    def save_queue(self):
        current = self.front
        pembeli_list = []

        while current:
            pembeli_list = pembeli_list + [current.data.to_dict()]
            current = current.next

        with open(self.file_path, "w") as file:
            json.dump(pembeli_list, file, indent=4)

    def enqueue(self, pembeli):
        new_node = Queue_Node(pembeli)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.save_queue()
    
    def is_empty(self):
        return self.top is None

    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        removed_node.next = None
        self.save_queue()
        return removed_node.data

    def display(self):
        current = self.front
        pembeli_list = []

        while current:
            pembeli_list = pembeli_list + [current.data.to_dict()]
            current = current.next

        return pembeli_list
