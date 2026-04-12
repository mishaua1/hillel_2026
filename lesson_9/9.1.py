class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side must be greater than 0")

        elif name == "angle_a":
            object.__setattr__(self, name, value)
            object.__setattr__(self, "angle_b", 180 - value)
            return

        elif name == "angle_b":
            raise AttributeError("angle_b cannot be set directly!")

        object.__setattr__(self, name, value)
