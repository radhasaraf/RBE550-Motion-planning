import argparse
import os
import random
from typing import Tuple

from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument(
    "--coverage", type=int, help="percentage of obstacle coverage in grid"
)
args = parser.parse_args()


COVERAGE = args.coverage
if not COVERAGE:
    print("Error: Coverage to use isn't specified.")
    os.abort()


TOTAL_PIXELS = 128 * 128


def get_coverage(image: Image):
    black_pixels = 0
    for pixel in image.getdata():
        if pixel != 0:
            continue
        black_pixels += 1

    return black_pixels / TOTAL_PIXELS


def place_tetromino_in_image(position: Tuple, tetromino_type: str, image):
    x = position[0]
    y = position[1]

    if tetromino_type == "1":  # I tetromino
        image.putpixel(position, 0)
        image.putpixel((x, y + 1), 0)
        image.putpixel((x, y + 2), 0)
        image.putpixel((x, y + 3), 0)

    elif tetromino_type == "2":  # L tetromino
        image.putpixel(position, 0)
        image.putpixel((x + 1, y), 0)
        image.putpixel((x + 1, y + 1), 0)
        image.putpixel((x + 1, y + 2), 0)

    elif tetromino_type == "3":  # Z tetromino
        image.putpixel(position, 0)
        image.putpixel((x, y + 1), 0)
        image.putpixel((x + 1, y + 1), 0)
        image.putpixel((x + 1, y + 2), 0)

    else:  # T tetromino
        image.putpixel((x + 1, y), 0)
        image.putpixel((x, y + 1), 0)
        image.putpixel((x + 1, y + 1), 0)
        image.putpixel((x + 1, y + 2), 0)

    return image


if __name__ == "__main__":
    grid = Image.new("1", (128, 128), color=1)

    desired_coverage = COVERAGE / 100

    current_coverage = 0
    while current_coverage < desired_coverage:

        random_x = random.randint(0, 124)
        random_y = random.randint(0, 124)
        random_tetromino_index = str(random.randint(1, 4))

        grid = place_tetromino_in_image(
            (random_x, random_y), random_tetromino_index, grid
        )
        current_coverage = get_coverage(grid)

    grid = grid.resize((600, 600))
    grid.save(f"Obstacle_course({COVERAGE}).jpeg")
    print("Obstacle course saved to image locally!")
