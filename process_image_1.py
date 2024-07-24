import sys
from PIL import Image

def resize_and_place_image(background_path, profile_path, output_path, position, size):
    # Open the background image
    background = Image.open(background_path)

    # Open the profile image
    profile = Image.open(profile_path)

    # Resize the profile image
    profile = profile.resize(size, Image.LANCZOS)

    # Paste the profile image onto the background
    background.paste(profile, position, profile if profile.mode == 'RGBA' else None)

    # Save the result
    background.save(output_path)

# Paths to the images
background_image_path = 'download.png'  # Path to the background image
profile_image_path = 'static/uploads/uploaded_image.png'        # Path to the profile image
output_image_path = 'output.png'          # Path to save the final image

# Position and size
position = (200, 400)  # Position to place the profile image (top-left corner)
size = (220, 220)      # Size to resize the profile image to (width, height)

# Call the function
resize_and_place_image(background_image_path, profile_image_path, output_image_path, position, size)
