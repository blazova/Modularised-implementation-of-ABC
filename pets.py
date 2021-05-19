from animals import Dog, Cat, Frog

if __name__ == "__main__":
    wiskers = Cat('Wiskers', 3)
    paws = Dog('Mr. Paws', 4, 'dachshund', 18)
    frosch = Frog('Mr. Frosch', 78, 'green')
    wiskers.speak()
    paws.speak()
    frosch.speak()