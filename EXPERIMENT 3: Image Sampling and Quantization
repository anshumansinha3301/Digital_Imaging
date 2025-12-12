import cv2

# Read the image in grayscale
img = cv2.imread("C:/Users/Surjit/OneDrive/Desktop/my.jpeg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded properly
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

# Apply threshold value 100
ret, binary = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

# Show the results
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image (Threshold = 100)", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
