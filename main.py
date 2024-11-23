from skimage import io, img_as_ubyte
from skimage.filters import gaussian
import os

def blur_image(input_folder, output_folder, sigma=5):
    """
    Apply Gaussian blur to an image and save the result in the output folder.

    Parameters:
        input_folder (str): Folder containing the input image.
        output_folder (str): Folder to save the blurred image.
        file_name (str): Name of the image file to process.
        sigma (float): Standard deviation for Gaussian kernel. Higher value = more blur.
    """
    # Construct the full input path
    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)

        if not (file_name.lower().endswith(('.png', '.jpg', '.jpeg'))):
            print(f"Skipping non-image file: {file_name}")

        # # Check if the image file exists
        # if not os.path.isfile(input_path):
        #     print(f"Error: Image file '{file_name}' not found in folder '{input_folder}'.")
        #     return

        # Load the image
        # try:
        #     image = io.imread(input_path)
        #     print(f"Loaded image '{file_name}' with shape: {image.shape}")
        # except Exception as e:
        #     print(f"Error loading image: {e}")
        #     return

        # Apply Gaussian blur
        try:
            image = io.imread(input_path)
            print(f"Loaded image '{file_name}' with shape: {image.shape}")

            blurred_image = gaussian(image, sigma=sigma)

            blurred_image = img_as_ubyte(blurred_image)

            os.makedirs(output_folder, exist_ok=True)

            output_path = os.path.join(output_folder, f"blurred_{file_name}")
            io.imsave(output_path, blurred_image)
            print(f"Blurred image save to: {output_path}")        
        except Exception as e:
            print(f"Error applying Gaussian blur: {e}")

# Define input/output folders and file name
input_folder = "resized-image"  # Take photo from Resized folder
# file_name = "2.jpg"  # Replace with the actual file name in your `images` folder
output_folder = "output_blurred_images"  # Folder to save blurred images

# Call the function to blur the image
blur_image(input_folder, output_folder, sigma=10)

