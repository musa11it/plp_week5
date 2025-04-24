class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def display_info(self):
        print(f"{self.name} belongs to {self.universe} and has the power of {self.power}.")

# Subclass to explore inheritance and encapsulation
class Mutant(Superhero):
    def __init__(self, name, power, universe, mutation_level):
        super().__init__(name, power, universe)
        self.__mutation_level = mutation_level  # encapsulated attribute

    def reveal_mutation(self):
        print(f"{self.name}'s mutation level is {self.__mutation_level}.")