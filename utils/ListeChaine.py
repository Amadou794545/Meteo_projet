class Node:
    def __init__(self, station_name, data):
        self.station_name = station_name
        self.data = data
        self.next = None  # Référence au nœud suivant


class LinkedList:
    def __init__(self):
        self.head = None  # Premier nœud de la liste

    def append(self, station_name, data):
        new_node = Node(station_name, data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"Station: {current.station_name}, Data: {current.data.head()}")
            current = current.next
