class Cat:
    likes_water = False

    @property
    def is_cute(self):
        return True


class Lion(Cat):
    pass


def create_exceptional_leopard():
    raise ValueError("Leopards are just normal!")


class Duck:
    def quack(self, volume):
        if volume < 0:
            return "..."
        if volume <= 20:
            return "quack"
        if volume <= 50:
            return "Quack"
        if volume <= 80:
            return "QUACK"
        return "QUAAAACK!"
