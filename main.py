import numpy as np
import math
from PIL import Image

# Create a NumPy array of zeros with dimensions 1000x1000 and 4 channels (RGBA)
empty_sheet = np.ones((1000, 1000, 4), dtype=int)

# Read data from the file
with open('data.txt', 'r') as file1:
    lines = file1.readlines()

# Get the dimensions and center coordinates of the image
w, h = empty_sheet.shape[1], empty_sheet.shape[0]
center_x, center_y = w // 2, h // 2


def polar_to_cartesian(angle, distance, center_x, center_y):
    """
    Convert polar coordinates to Cartesian coordinates.

    Args:
    - angle (float): Angle in degrees.
    - distance (float): Distance from the origin.
    - center_x (int): X coordinate of the center.
    - center_y (int): Y coordinate of the center.

    Returns:
    - (int, int): Cartesian coordinates (x, y).
    """
    angle_radiance = math.radians(angle)
    x_coordinate = int(center_x + distance * math.cos(angle_radiance))
    y_coordinate = int(center_y - distance * math.sin(angle_radiance))
    return x_coordinate, y_coordinate


# Process each line and convert the coordinates
for line in lines:
    parts = line.strip().split("->")[1].split(":/:")
    angle = float(parts[0])
    distance = float(parts[1])
    x, y = polar_to_cartesian(angle, distance, center_x, center_y)

    # Check if coordinates are within image boundaries
    if 0 <= x < w and 0 <= y < h:
        empty_sheet[y, x] = (255, 0, 0, 255)  # Set pixel to red in RGBA format

# Convert the NumPy array to a PIL Image
image = Image.fromarray(np.uint8(empty_sheet), 'RGBA')

# Save and show the image
image.show()
image.save('output_image.png')

