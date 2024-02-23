from handle_url_form import WebClientApp
from edge_detection import EdgeDetection

class MainApp:
    def __init__(self):
        pass

    def run(self):
        # Start the Flask server for handling URL form
        handle_url_form = WebClientApp()
        handle_url_form.run()

        # Perform edge detection
        
        if (handle_url_form.get_saved_url()):
            url = handle_url_form.get_saved_url()
            edge_detection = EdgeDetection(url)
            edge_detection.download_image()
            edge_detection.detect_edges()
        else:
            handle_url_form.run()
            print("Waiting for your URL ...")

if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()