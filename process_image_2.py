import sys
from PIL import Image, ImageDraw, ImageFont

def add_texts_to_image(image_path, texts, positions, font_paths, font_sizes, colors, output_path):
    # Open an image file
    with Image.open(image_path) as image:
        # Initialize ImageDraw
        draw = ImageDraw.Draw(image)
        
        # Loop over each text and its corresponding position, font path, font size, and color
        for text, position, font_path, font_size, color in zip(texts, positions, font_paths, font_sizes, colors):
            # Load the appropriate font
            font = ImageFont.truetype(font_path, font_size)
            # Draw text on the image
            draw.text(position, text, font=font, fill=color)
        
        # Save the edited image
        image.save(output_path)
        print(f"Image saved as {output_path}")

def main():
    # Input the names from the user
    name1 = sys.argv[1]
    name2 = sys.argv[2]
    name3 = sys.argv[3]

    # Example usage:
    image_path = 'output.png'    # Path to the input image
    texts = [name1,name2,name3]  # List of texts to be written on the image
    positions = [(200, 620), (290, 703), (260, 750)]    # List of positions to place the texts (x, y)
    font_paths = ['Staatliches.ttf', 'Staatliches.ttf', 'Staatliches.ttf']  # List of paths to the .ttf font files
    font_sizes = [75, 46, 35]  # List of font sizes for each text
    colors = ['rgb(255, 251, 254)', 'rgb(255, 251, 254)', 'rgb(255, 199, 46)']  # List of colors for the texts
    output_path = 'static/output_image.png'  # Path to save the new image

    # Call the function to add names to the image
    add_texts_to_image(image_path, texts, positions, font_paths, font_sizes, colors, output_path)

# Run the main function
if __name__ == "__main__":
    main()