import cv2
import urllib.request
import ssl

class EdgeDetection:
    def __init__(self):
        self.url = self.read_url_from_file()

    def read_url_from_file(self):
        try:
            with open('url.txt', 'r') as f:
                
                return f.read().strip()
        except FileNotFoundError:
            print("URL file not found.")
            return None
        
    def download_image(self):
        # Disable SSL certificate verification
        ssl._create_default_https_context = ssl._create_unverified_context

        # Open the URL
        req = urllib.request.urlopen(self.url)

        # Read the content
        image_data = req.read()

        # Save the image
        with open("target_img.jpg", "wb") as f:
            f.write(image_data)

        print("Image downloaded successfully!")

    def detect_edges(self):
        # Load the image
        image = cv2.imread('target_img.jpg')
        image = cv2.resize(image, (900,1200))
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

if __name__ == "__main__":
    edge_detection = EdgeDetection()
    print("Received URL: ", edge_detection.url)
    edge_detection.download_image()
    edge_detection.detect_edges()
