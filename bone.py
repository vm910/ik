import numpy as np

from pygame import Vector2


class Bone:
    def __init__(self, a: Vector2, length: float) -> None:
        self.a = a
        self.angle = 0
        self.length = length

    @property
    def b(self) -> Vector2:
        return Vector2(
            self.a.x + self.length * np.cos(self.angle),
            self.a.y + self.length * np.sin(self.angle),
        )

    def rotate_and_translate(self, target: Vector2):
        self.rotate(target)

        self.a.update(
            target.x - self.length * np.cos(self.angle),
            target.y - self.length * np.sin(self.angle),
        )

    def rotate(self, target: Vector2):
        dir = target - self.a
        self.angle = np.arctan2(dir.y, dir.x)
