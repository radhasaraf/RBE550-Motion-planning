import argparse
import os
import random
from typing import Tuple

import matplotlib.pyplot as plt
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument(
    "--coverage", type=int, help="percentage of obstacle coverage in grid"
)
parser.add_argument(
    "--save", type=bool, help="whether to save figure to image(default: False)"
)

args = parser.parse_args()

COVERAGE = args.coverage
if not COVERAGE:
    print("Error: Coverage to use isn't specified.")
    os.abort()


def get_coverage(image: Image, size_in_pixels: int) -> float:
    black_pixels = 0
    for pixel in image.getdata():
        if pixel != 0:
            continue
        black_pixels += 1

    return black_pixels / size_in_pixels ** 2


def place_tetromino_in_image(position: Tuple, tetromino_type: str, image) -> Image:
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


def create_obstacle_grid(grid_size: int = 128, coverage: int = 5, **kwargs) -> Image:
    print(
        f"Creating obstacle grid({grid_size}x{grid_size}) with coverage of {coverage}%"
    )
    grid = Image.new("1", (grid_size, grid_size), color=1)
    desired_coverage = coverage / 100

    current_coverage, window_index = 0, 0
    while current_coverage < desired_coverage:
        window_index += 1

        random_x = random.randint(0, 124)
        random_y = random.randint(0, 124)
        random_tetromino_index = str(random.randint(1, 4))

        grid = place_tetromino_in_image(
            (random_x, random_y), random_tetromino_index, grid
        )
        current_coverage = get_coverage(grid, grid_size)

        plt.imshow(grid)
        plt.axis("off")
        if (
            window_index % kwargs.get("pause_interval", 3) == 0
        ):  # Pauses only occasionally for faster updates
            plt.pause(0.001)  # Updates the active fig & displays it before the pause

    if kwargs.get("save", False):
        plt.savefig(f"Obstacle_course({COVERAGE}).jpeg", bbox_inches="tight")
        print("Obstacle course saved to image locally!")

    plt.show()  # Causes the image fig to persist after completion
    return grid


if __name__ == "__main__":
    create_obstacle_grid(coverage=COVERAGE, save=args.save)
