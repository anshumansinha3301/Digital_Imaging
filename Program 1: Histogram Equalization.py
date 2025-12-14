import cv2
import matplotlib.pyplot as plt

# Path to your image
path = r"C:\Users\Surjit\OneDrive\Desktop\my.jpeg"

# Read the image in grayscale
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Check if the image loaded correctly
if img is None:
    print("Error: Unable to load image. Check the file path.")
    exit()

# Apply histogram equalization
equalized = cv2.equalizeHist(img)

# Display results using matplotlib
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

# Equalized image
plt.subplot(1, 2, 2)
plt.title("Equalized")
plt.imshow(equalized, cmap='gray')
plt.axis('off')

plt.show()
