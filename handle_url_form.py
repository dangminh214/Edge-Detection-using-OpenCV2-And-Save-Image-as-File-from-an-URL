from flask import Flask, request, render_template
import time
import cv2
import urllib.request
import ssl

class EdgeDetection:
    def __init__(self, url):
        self.url = url

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
        image = cv2.resize(image, (900, 1200))
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

class WebClientApp:
    def __init__(self, name_main_page='webclient_inputURL.html'):
        self.name_main_page = name_main_page
        self.app = Flask(__name__)
        self.edge_detection = None

        @self.app.route('/')
        def index():
            return render_template(self.name_main_page)

        @self.app.route('/save-url', methods=['POST'])
        def save_url():
            url = request.form['url']
            with open('url.txt', 'w') as f:
                f.write(url)
            print(f'This is your URL: "{url}", saved successfully.')
            
            # Initialize EdgeDetection and process image
            self.edge_detection = EdgeDetection(url)
            self.edge_detection.download_image()
            self.edge_detection.detect_edges()

            return f'This is your URL: "{url}", saved successfully.'

    def run(self):
        if __name__ == '__main__':
            self.app.run(debug=True)

if __name__ == '__main__':
    web_client_app = WebClientApp()
    web_client_app.run()
