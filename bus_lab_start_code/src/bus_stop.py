class BusStop:
    def __init__(self, name) -> None:
        self.name = name
        self.queue = []
        
    def add_to_queue(self, person):
        self.queue.append(person)