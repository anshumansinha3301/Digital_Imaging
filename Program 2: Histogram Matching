from skimage import exposure, io
import matplotlib.pyplot as plt

# Path to the image
path = r"C:\Users\Surjit\OneDrive\Desktop\my.jpeg"

# Read source and reference images (same image for demonstration)
source = io.imread(path, as_gray=True)
reference = io.imread(path, as_gray=True)

# Check if images loaded correctly
if source is None or reference is None:
    print("Error: Unable to load image. Check the file path.")
    exit()

# Apply histogram matching
matched = exposure.match_histograms(source, reference)

# Display the results
plt.figure(figsize=(12, 4))

# Source image
plt.subplot(1, 3, 1)
plt.title("Source")
plt.imshow(source, cmap='gray')
plt.axis('off')

# Reference image
plt.subplot(1, 3, 2)
plt.title("Reference")
plt.imshow(reference, cmap='gray')
plt.axis('off')

# Histogram-matched image
plt.subplot(1, 3, 3)
plt.title("Matched")
plt.imshow(matched, cmap='gray')
plt.axis('off')

plt.show()
