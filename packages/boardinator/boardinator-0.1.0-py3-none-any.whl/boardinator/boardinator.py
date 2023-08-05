"""Generate a chess board from given colors"""

import argparse
import ast
import os

import numpy as np
from PIL import Image


def replace_colors(
    image_path,
    color_dict,
    output_path="output.png",
    show=False,
):
    """Replace colors in an image. Supports PNG and SVG formats."""
    # Load the image and convert it to RGBA
    img = Image.open(image_path)
    img = img.convert("RGBA")

    data = np.array(img)
    red, green, blue, alpha = data.T
    # rgba(119, 153, 82, 1)
    # target_areas = (red == 119) & (green == 153) & (blue == 82) & (alpha == 255)
    # data[..., :-1][target_areas.T] = (255, 0, 0)

    # Replace colors
    for old_color, new_color in color_dict.items():
        target_areas = (
            (red == old_color[0])
            & (green == old_color[1])
            & (blue == old_color[2])
            & (alpha == 255)
        )
        data[..., :-1][target_areas.T] = new_color

    img2 = Image.fromarray(data)

    # Save modified image
    if show:
        img2.show()
    img2.save(output_path, "PNG")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replace colors in an image")
    parser.add_argument(
        "--input_path",
        type=str,
        default=os.path.join(os.path.dirname(__file__), "assets/chesscom.png"),
        help="path to input image (default: ./assets/chess.com.png)",
    )
    parser.add_argument(
        "--output_path", type=str, required=True, help="path to output image"
    )
    parser.add_argument(
        "--color_dict", type=str, default="{}", help="dictionary of color replacements"
    )
    parser.add_argument("--show", action="store_true", help="show the image")

    args = parser.parse_args()

    color_dict_arg = ast.literal_eval(args.color_dict)
    color_dict_arg = {
        tuple(ast.literal_eval(k)): tuple(ast.literal_eval(v))
        for k, v in color_dict_arg.items()
    }
    replace_colors(
        image_path=args.input_path,
        output_path=args.output_path,
        color_dict=color_dict_arg,
        show=args.show,
    )
#
