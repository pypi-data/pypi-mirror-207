# Chess Boardinator

This project generates a chess board image from a given input image by replacing specific colors with new ones. The output image is saved to a file specified by the user. The project supports PNG and SVG formats.

## Usage

```
boardinator --show --output_path cool_image.png --color_dict '{"(237,238,209)":"(0,0,255)","(119,153,82)":"(0,0,0)"}'
```

### Arguments

-   `--input_path`: path to the input image file (default: `./assets/chesscom.png`)
-   `--output_path`: path to the output image file (required)
-   `--color_dict`: dictionary of color replacements in string format (default: `{}`)
-   `--show`: flag to show the modified image

## Installation

This project requires Python 3.11 or later and can be installed using [Poetry](https://python-poetry.org/).

1. Clone the repository:

```
git clone https://github.com/example/chess-boardinator.git
cd chess-boardinator
```

2. Install dependencies using Poetry:

```
poetry install
```

3. Run the project:

```
poetry run boardinator --show --output_path cool_image.png --color_dict '{"(237,238,209)":"(0,0,255)","(119,153,82)":"(0,0,0)"}'
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
