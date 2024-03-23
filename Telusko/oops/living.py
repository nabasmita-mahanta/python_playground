class LivingThing:
    has_life = True

    def __init__(self, life):
        self.life_expectancy = life

    def breathe(self):
        print("I am alive and breathing")
