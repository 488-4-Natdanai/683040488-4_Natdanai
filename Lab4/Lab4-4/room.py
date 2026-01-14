from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    @abstractmethod
    def get_purpose(self):
        pass

    @abstractmethod
    def get_recommended_lighting(self):
        pass

    def calculate_area(self):
        return self.length * self.width
    
    def describe_room(self):
        area = self.calculate_area()
        return f"A {self.__class__.__name__} of {area} sq ft used for {self.get_purpose()}"


class Bedroom(Room):
    def __init__(self, length, width, bed_size):
        super().__init__(length, width)
        self.bed_size = bed_size

    def get_purpose(self):
        return "sleeping and relaxing"

    def get_recommended_lighting(self):
        return 15   # lumens per sq ft (reasonable bedroom lighting)


class Kitchen(Room):
    def __init__(self, length, width, has_island=True):
        super().__init__(length, width)
        self.has_island = has_island

    def get_purpose(self):
        return "cooking and food preparation"

    def get_recommended_lighting(self):
        return 40   # lumens per sq ft (reasonable kitchen lighting)

    def calculate_counter_space(self):
        area = self.calculate_area()

        if self.has_island:
            island = area / 5
            wall = area / 4
        else:
            island = 0
            wall = area / 2

        return island, wall
