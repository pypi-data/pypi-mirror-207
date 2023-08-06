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
    # Load the image
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: file '{image_path}' not found.")

    # Define the ending pixel size of the pixelation effect
    end_pixel_size = 0

    if start_pixel_size <= end_pixel_size:
        raise ZeroDivisionError("start_pixel_size must be greater than end_pixel_size.")

    # Create a list to hold the frames of the GIF
    frames = []

    if not reverse:
        # Add the non-pixelated image to the frames list
        frames.append(image)

        # Apply the pixelation effect to the image and add it to the frames list
        for pixel_size in range(end_pixel_size + 1, start_pixel_size):
            # Resize the image to the pixelated size
            small_image = image.resize((image.width // pixel_size, image.height // pixel_size), resample=Image.BOX)

            # Scale the pixelated image back up to its original size
            pixelated_image = small_image.resize(image.size, resample=Image.NEAREST)

            # Add the pixelated image to the frames list
            frames.append(pixelated_image)

    else:
        # Apply the pixelation effect to the image and add it to the frames list
        for pixel_size in range(start_pixel_size, end_pixel_size - 1, -1):
            if pixel_size == 0:
                continue

            # Resize the image to the pixelated size
            small_image = image.resize((image.width // pixel_size, image.height // pixel_size), resample=Image.BOX)

            # Scale the pixelated image back up to its original size
            pixelated_image = small_image.resize(image.size, resample=Image.NEAREST)

            # Add the pixelated image to the frames list
            frames.append(pixelated_image)

        # Add the non-pixelated image to the frames list
        frames.append(image)

    # Set the output file path
    if not output_path:
        output_path = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(image_path))[0] + '.gif')

    # Save the frames as a GIF
    imageio.mimsave(output_path, frames, duration=duration, loop=loops)

    return output_path
