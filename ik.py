import sys, pygame

from bone import Bone
from pygame.math import Vector2

pygame.init()

shape = width, height = 1500, 850
screen = pygame.display.set_mode(shape)


def draw(bones: list[Bone], target: Vector2):
    black = 0, 0, 0
    white = 255, 255, 255

    screen.fill(white)

    for bone in bones:
        pygame.draw.aaline(screen, black, bone.a, bone.b)

    pygame.draw.circle(screen, black, (int(target[0]), int(target[1])), 2)
    pygame.display.flip()


def IK(bones: list[Bone], target: Vector2):
    i = len(bones) - 2

    if len(bones) > 1:
        bones[-1].rotate_and_translate(target)
    else:
        bones[-1].rotate(target)

    while i >= 0:
        if i != 0:
            bones[i].rotate_and_translate(bones[i + 1].a)
        else:
            bones[i].rotate(bones[i + 1].a)
        i -= 1

    for i in range(1, len(bones)):
        bones[i].a = bones[i - 1].b

    return bones


def get_lengths(path: str) -> list[float]:
    with open(path) as f:
        return eval(f.read())


def init_bones(lengths: list[float]) -> list[Bone]:
    root = Bone(Vector2(width / 2, height / 2), lengths[0])
    bones = [root]

    for i in range(1, len(lengths)):
        bones.append(Bone(bones[i - 1].b, lengths[i]))

    return bones


def main():
    lengths = get_lengths("input_lengths.txt")
    bones = init_bones(lengths)

    while 1:
        target = Vector2(pygame.mouse.get_pos())
        bones = IK(bones, target)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        draw(bones, target)


if __name__ == "__main__":
    main()
