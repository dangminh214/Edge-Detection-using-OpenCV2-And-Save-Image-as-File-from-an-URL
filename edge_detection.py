import cv2
import urllib.request
import ssl
#****************** DOWNLOAD SECTION ****************************************************
# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# URL of the image
url = "https://softwarebydefault.files.wordpress.com/2013/05/monarch_in_may.jpg"

# Open the URL
req = urllib.request.urlopen(url)

# Read the content
image_data = req.read()

# Save the image
with open("target_img.jpg", "wb") as f:
    f.write(image_data)

print("Image downloaded successfully!")
# ********************* EDGE DETECTION SECTION ********************************************
# Load the image
image = cv2.imread('target_img.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()