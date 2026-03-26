from datetime import datetime

class Cat:
    species = "Felis catus"
    total_cats = 0
    average_lifespan = 15

    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

        self.hungry = False
        self.energy = 100
        self.happiness = 100

        Cat.total_cats += 1

    def meow(self):
        if self.hungry:
            return f"{self.name} meows loudly: MEOW!!! (I'm hungry!)"
        elif self.energy < 30:
            return f"{self.name} meows softly: meow..."
        else:
            return f"{self.name} happily says: Meow~"

    def eat(self, food_amount):
        if food_amount <= 0:
            return f"{self.name} refuses to eat."

        self.hungry = False
        self.energy = min(100, self.energy + food_amount * 2)
        self.happiness = min(100, self.happiness + food_amount)

        return f"{self.name} eats {food_amount}g of food."

    def play(self, play_time):
        if play_time <= 0:
            return f"{self.name} doesn't want to play."

        energy_loss = play_time * 10
        happiness_gain = play_time * 15

        self.energy = max(0, self.energy - energy_loss)
        self.happiness = min(100, self.happiness + happiness_gain)

        if self.energy < 20:
            self.hungry = True

        return f"{self.name} plays for {play_time} hours."

    def sleep(self, hours):
        if hours <= 0:
            return f"{self.name} can't sleep."

        self.energy = min(100, self.energy + hours * 20)
        self.hungry = True

        return f"{self.name} sleeps for {hours} hours."

    def get_status(self):
        return {
            "name": self.name,
            "age": self.age,
            "breed": self.breed,
            "color": self.color,
            "hungry": self.hungry,
            "energy": self.energy,
            "happiness": self.happiness
        }

    @classmethod
    def from_birth_year(cls, name, birth_year, breed, color):
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age, breed, color)

    @classmethod
    def get_species_info(cls):
        return {
            "species": cls.species,
            "average_lifespan": cls.average_lifespan,
            "total_cats": cls.total_cats
        }

    @staticmethod
    def is_senior(age):
        return age > 7

    @staticmethod
    def calculate_healthy_food_amount(weight_kg):
        return weight_kg * 20
