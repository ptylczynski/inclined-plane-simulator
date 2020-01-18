from math import sin, cos, atan

from maths.function import Function
from maths.inputMonoFunction import InputMonoFunction


class Gravity(InputMonoFunction):
    def __init__(self, expression: str):
        super().__init__(expression)


class Friction(InputMonoFunction):
    def __init__(self, expression: str):
        super().__init__(expression)


class Plane(InputMonoFunction):
    def __init__(self, expression: str):
        super().__init__(expression)


class Angle(Function):
    def __init__(self, plane: Plane):
        super().__init__()
        self.plane: Plane = plane

    def evaluate(self, arg):
        return -atan((self.plane[arg] - self.plane[arg - 0.00000001]) / 0.00000001)


class FrictionAcceleration(Function):
    def __init__(self, gravity: Gravity, friction: Friction, angle: Angle):
        super().__init__()
        self.gravity: Gravity = gravity
        self.friction: Friction = friction
        self.angle: Angle = angle

    def evaluate(self, arg):
        return self.gravity[arg] * cos(self.angle[arg]) * self.friction[arg]


class GravityAcceleration(Function):
    def __init__(self, gravity: Gravity, friction: Friction, angle: Angle):
        super().__init__()
        self.gravity: Gravity = gravity
        self.friction: Friction = friction
        self.angle: Angle = angle

    def evaluate(self, arg):
        return self.gravity[arg] * sin(self.angle[arg])
