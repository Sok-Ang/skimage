import os
import numpy as np
from skimage import io, img_as_ubyte
from skimage.transform import resize

def resize_image(input_folder, output_folder,):
    """
    Resizes an input image to 250x250x3 and saves it to the output folder.

    Parameters:
        input_folder (str): Folder containing the input image.
        output_folder (str): Folder to save the resized image.
        file_name (str): Name of the image file to process.
    """
    # Create a 250x250x5 numpy.zeros array for demonstration
    blank_array = np.zeros((250, 250, 5), dtype=np.float64)
    print(f"Created blank array with shape: {blank_array.shape} and dtype: {blank_array.dtype}")

    # Input image path
    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)

        # Check if the image file exists
        if not os.path.isfile(input_path):
            print(f"Error: Image file '{file_name}' not found in folder '{input_folder}'.")
            return

        # Load the input image
        try:
            image = io.imread(input_path)
            print(f"Loaded image '{file_name}' with shape: {image.shape}")
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        # Resize the image to 250x250x3
        try:
            resized_image = resize(image, (250, 250, 3), anti_aliasing=True)
        except Exception as e:
            print(f"Error resizing image: {e}")
            return

        # Convert resized image to 8-bit unsigned integers
        resized_image = img_as_ubyte(resized_image)

        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Save the resized image
        output_path = os.path.join(output_folder, file_name)
        try:
            io.imsave(output_path, resized_image)
            print(f"Resized image saved to: {output_path}")
        except Exception as e:
            print(f"Error saving image: {e}")

# Define folders and file name
input_folder = "images2"  # Folder containing input images
output_folder = "resized-image"  # Folder to save resized images
# file_name = "1.jpg"  # Replace with the actual file name in your `images` folder

# Call the function to resize the image
resize_image(input_folder, output_folder)
