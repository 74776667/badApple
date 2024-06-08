import cv2
import os

# Function to extract frames from video
def extract_frames(video_path, output_folder, interval=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    print(f"Total frames: {frame_count}")
    print(f"FPS: {fps}")

    frame_index = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_index % interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{frame_index}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved: {frame_filename}")

        frame_index += 1

    cap.release()
    print("Done extracting frames.")

# Function to pixelate an image with custom height and width
def pixelate_image(image, pixel_size=10, custom_width=None, custom_height=None):
    height, width = image.shape[:2]

    # Resize input to "pixel_size" using nearest neighbor interpolation
    temp = cv2.resize(image, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_NEAREST)

    # Scale it back to original size
    pixelated_image = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

    # Resize to custom dimensions if provided
    if custom_width and custom_height:
        pixelated_image = cv2.resize(pixelated_image, (custom_width, custom_height), interpolation=cv2.INTER_NEAREST)

    return pixelated_image

# Function to pixelate frames in a folder with custom dimensions
def pixelate_frames(input_folder, output_folder, pixel_size=10, custom_width=None, custom_height=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            input_path = os.path.join(input_folder, filename)
            image = cv2.imread(input_path)

            if image is None:
                continue

            pixelated_image = pixelate_image(image, pixel_size, custom_width, custom_height)
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, pixelated_image)
            print(f"Pixelated and saved: {output_path}")

    print("Done pixelating frames.")

# Usage
video_path = 'PATH'
output_frames_folder = 'PATH'
pixelated_frames_folder = 'PATH'
frame_interval = 1  # Save one frame every 10 frames
pixel_size = 10  # Size of the pixels in the pixelated image
custom_width = 11  
custom_height = 5 

#11X5 Screen on Instagram notes!

# Step 1: Extract frames from video
extract_frames(video_path, output_frames_folder, frame_interval)

# Step 2: Pixelate extracted frames with custom dimensions
pixelate_frames(output_frames_folder, pixelated_frames_folder, pixel_size, custom_width, custom_height)
