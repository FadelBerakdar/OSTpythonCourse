from BirdAPI import Bird


class Flock(object):
    birds = []

    def add_bird(self, bird):
        """
        Add bird object to the flock
        """
        self.birds.append(bird)

    def race(self):
        """
        Show how far the birds of the flock can go in one hour carrying their
        respective food.
        """
        print("Distance flown in one hour by the flock")
        for bird in self.birds:
            distance = "-" * int((bird.calculate()//10))
            notice = "%s: %s carrying %s items" % (distance, bird.name,
                                                   len(bird.__dict__))
            print(notice)

if __name__ == "__main__":
    swallow = Bird(coconut=1, name="Swallow")

    african = Bird(coconut=1, piece="of string", visited=False,
                   name="African Swallow")

    european = Bird(coconut=1, lottery_numbers=(23, 12, 34), piece="of string",
                    visited=True, name="European Swallow")

    birds = (
        ("Swallows are a group of birds in the family Hirundinidae.", swallow),
        ("African swallows are said to be able to carry coconuts.", african),
        ("European swallows are said to have trouble carrying coconuts.", european)
        )

    flock = Flock()
    for statement, bird in birds:
        print(statement)
        flock.add_bird(bird)
    flock.race()



