from .animal import Animal

class Frog(Animal):

    def __init__(self, name:str, age:int, color:str):
        """Create a new dog"""
        self.color = color
        super().__init__(name, age)
        
    def speak(self) -> None:
        """Make the frog peep"""
        print(f'{self.name} says, "peep"')
