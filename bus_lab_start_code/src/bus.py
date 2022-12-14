class Bus:
    def __init__(self, route_number, destination) -> None:
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        """theory of why .remove is an issue if for loop
        counter = 1
        test = [1, 2]
        for p in bus_stop.queue:
            print("this is: ", test)
            self.pick_up(p)
            test.remove(counter)
            counter += 1
            print(test)
            bus_stop.join_bus()"""

        while bus_stop.queue:
            self.pick_up(bus_stop.queue[0])
            bus_stop.queue.remove(bus_stop.queue[0])
