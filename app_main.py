from handle_url_form import WebClientApp
from edge_detection import EdgeDetection
import threading

class MainApp:
    def __init__(self):
        pass

    def run(self):
        # Start the Flask server for handling URL form
        handle_url_form = WebClientApp()
    # handle_url_form.run()
        server_thread = threading.Thread(target=handle_url_form.run)  # Run Flask app in a separate thread
        server_thread.start()

        # Perform edge detection
        url = handle_url_form.get_saved_url()
        if (url):
            print("Saved URL: ", url)
            edge_detection = EdgeDetection()
            edge_detection.download_image()
            edge_detection.detect_edges()
        else:
            print("Waiting for your URL ...")

if __name__ == "__main__":
    main_app = MainApp()
    WebClientApp.get_saved_url
    main_app.run()