import argparse
import os
import random
from typing import Tuple

import matplotlib.pyplot as plt
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("--grid_size", type=int, help="grid size in pixels")
parser.add_argument(
    "--coverage", type=int, help="percentage of obstacle coverage in grid"
)
parser.add_argument(
    "--display", type=bool, help="whether to display grid during creation"
)
parser.add_argument(
    "--save", type=bool, help="whether to save figure to image(default: False)"
)
args = parser.parse_args()

obstacle_color = (0, 0, 0)
# obstacle_color = 0  # This also works for non-binary images


def get_coverage(image: Image, size_in_pixels: int) -> float:
    black_pixels = 0
    for pixel in image.getdata():
        if pixel != (0, 0, 0):
            continue
        black_pixels += 1

    return black_pixels / size_in_pixels ** 2


def place_tetromino_in_image(position: Tuple, tetromino_type: str, image) -> Image:
    x = position[0]
    y = position[1]

    if tetromino_type == "1":  # I tetromino
        image.putpixel(position, obstacle_color)
        image.putpixel((x, y + 1), obstacle_color)
        image.putpixel((x, y + 2), obstacle_color)
        image.putpixel((x, y + 3), obstacle_color)

    elif tetromino_type == "2":  # L tetromino
        image.putpixel(position, obstacle_color)
        image.putpixel((x + 1, y), obstacle_color)
        image.putpixel((x + 1, y + 1), obstacle_color)
        image.putpixel((x + 1, y + 2), obstacle_color)

    elif tetromino_type == "3":  # Z tetromino
        image.putpixel(position, obstacle_color)
        image.putpixel((x, y + 1), obstacle_color)
        image.putpixel((x + 1, y + 1), obstacle_color)
        image.putpixel((x + 1, y + 2), obstacle_color)

    else:  # T tetromino
        image.putpixel((x + 1, y), obstacle_color)
        image.putpixel((x, y + 1), obstacle_color)
        image.putpixel((x + 1, y + 1), obstacle_color)
        image.putpixel((x + 1, y + 2), obstacle_color)

    return image


def create_obstacle_grid(grid_size: int = 128, coverage: int = 5, **kwargs) -> Image:
    print(
        f"Creating obstacle grid({grid_size}x{grid_size}) with coverage of {coverage}%"
    )
    grid = Image.new("RGB", (grid_size, grid_size), color=(255, 255, 255))

    desired_coverage = coverage / 100

    current_coverage, window_index = 0, 0
    while current_coverage < desired_coverage:
        window_index += 1

        random_x = random.randint(0, grid_size - 4)
        random_y = random.randint(0, grid_size - 4)
        random_tetromino_index = str(random.randint(1, 4))

        grid = place_tetromino_in_image(
            (random_x, random_y), random_tetromino_index, grid
        )
        current_coverage = get_coverage(grid, grid_size)

        plt.imshow(grid)  # Required to render image on plot
        if kwargs.get("display"):
            plt.axis("off")
            if (
                window_index % kwargs.get("pause_interval", 3) == 0
            ):  # Pauses only occasionally for faster updates
                plt.pause(
                    0.001
                )  # Updates the active fig & displays it before the pause

    if kwargs.get("save", False):
        plt.savefig(f"Obstacle_course({coverage}).jpeg", bbox_inches="tight")
        print("Obstacle course saved to image locally!")

    if kwargs.get("display"):
        plt.show()  # Causes the image fig to persist after completion
    return grid


if __name__ == "__main__":

    grid_size = args.grid_size
    if not grid_size:
        grid_size = 128

    coverage = args.coverage
    if not coverage:
        print("Error: Coverage to use isn't specified.")
        os.abort()

    create_obstacle_grid(
        grid_size=grid_size, coverage=coverage, save=args.save, display=args.display
    )
