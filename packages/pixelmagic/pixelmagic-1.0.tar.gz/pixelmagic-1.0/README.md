# pixelmagic

`pixelmagic` is a Python package for creating pixelated GIFs from image files.

## Installation

To install the package, run the following command:

```markdown
pip install pixelmagic
```
Check if required packages are installed and install them if necessary:

```python
import os
import subprocess


def install(package):
    subprocess.check_call(['pip', 'install', package])


# Check if required packages are installed and install them if necessary
try:
    import imageio
except ImportError:
    install('imageio')
    import imageio

try:
    from PIL import Image
except ImportError:
    install('Pillow')
    from PIL import Image
```

## Usage
Here's an example of how to create a pixelated GIF using `pixelmagic`:

```python
from pixelmagic.pixelmagic import create_pixelated_gif

image_path = 'path/to/image.jpg'
duration = 0.1
loops = 0
start_pixel_size = 20
output_path = 'path/to/output.gif'
reverse = False  # Optional

create_pixelated_gif(image_path, duration, loops, start_pixel_size, output_path, reverse)
```

## Function Reference
```python
def create_pixelated_gif(image_path: str, duration: float, loops: int, start_pixel_size: int = 20,
                         output_path: str = '', reverse: bool = False) -> str:
    """Create a pixelated GIF from an image file and save it to disk.

    Args:
        image_path (str): The path to the image file.
        duration (float): The duration of each frame in the GIF.
        loops (int): The number of times the GIF should loop. Use 0 for infinite loops.
        start_pixel_size (int): The starting pixel size of the pixelation effect. Default is 20.
        output_path (str): The path to the output file. If not specified, the GIF will be saved to the root directory.
        reverse (bool): If True, the function will create a GIF that transitions from the pixelated image to the
        original image.

    Returns:
        str: The path to the output file. The pixelated GIF is saved to disk.

    Raises:
        FileNotFoundError: If the image file does not exist.
        ZeroDivisionError: If the start_pixel_size is less than or equal to the end_pixel_size.

    """
```

## License

`pixelmagic` is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Error Handling

`create_pixelated_gif` raises a `FileNotFoundError` if the image file does not exist, and a `ZeroDivisionError` if the `start_pixel_size` is less than or equal to the `end_pixel_size`.
