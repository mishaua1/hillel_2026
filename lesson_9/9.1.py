class Ромб:
    def __init__(self, сторона_а, кут_а):
        self.сторона_а = сторона_а
        self.кут_а = кут_а

    def __setattr__(self, name, value):
        if name == "сторона_а":
            if value <= 0:
                raise ValueError("Сторона повинна бути більше 0")

        elif name == "кут_а":
            object.__setattr__(self, name, value)
            object.__setattr__(self, "кут_б", 180 - value)
            return

        object.__setattr__(self, name, value)