import cv2
import os

# Emoji characters used to build the output text (use black and white emojis)
EMOJI_CHARS = ["⬛", "⬜"]

def resize_image(image, new_width, new_height):
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

def binarize_image(image, threshold=128):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply binary threshold
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

def pixels_to_emoji(image):
    emoji_str = ""
    for row in image:
        for pixel in row:
            emoji_str += EMOJI_CHARS[pixel // 128]
        emoji_str += "\n"
    return emoji_str

def convert_image_to_emoji(image_path, output_path, new_width, new_height):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Unable to open {image_path}")
        return

    # Binarize image
    binary_image = binarize_image(image)

    # Resize image
    resized_image = resize_image(binary_image, new_width, new_height)

    # Convert pixels to emojis
    emoji_image = pixels_to_emoji(resized_image)

    # Save emoji art to a text file with UTF-8 encoding
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(emoji_image)

    print(f"Converted {image_path} to emoji art and saved as {output_path}")

def process_folder(input_folder, output_folder, new_width, new_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
            convert_image_to_emoji(input_path, output_path, new_width, new_height)

    print("Done converting images to emoji art.")

# Usage
pixelated_frames_folder = 'PATH'
emoji_art_folder = 'PATH'
emoji_width = 11  
emoji_height = 5  

# Convert pixelated frames to emoji art
process_folder(pixelated_frames_folder, emoji_art_folder, emoji_width, emoji_height)
