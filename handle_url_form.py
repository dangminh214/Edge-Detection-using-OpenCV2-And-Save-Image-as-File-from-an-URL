from flask import Flask, request, render_template

class WebClientApp:
    def __init__(self, name_main_page='webclient_inputURL.html'):
        self.name_main_page = name_main_page
        self.app = Flask(__name__)

        @self.app.route('/')
        def index():
            return render_template(self.name_main_page)

        @self.app.route('/save-url', methods=['POST'])
        def save_url():
            url = request.form['url']
            with open('url.txt', 'w') as f:
                f.write(url)
            return f'This is your URL: "{url}", saved successfully.'

    def run(self):
        if __name__ == '__main__':
            self.app.run(debug=True)

    def get_saved_url(self):
        try:
            with open('url.txt', 'r') as f:
                url = f.read().strip()
            return url
        except FileNotFoundError:
            print("URL file not found.")
            return None

if __name__ == '__main__':
    web_client_app = WebClientApp()
    web_client_app.run()
    saved_url = web_client_app.get_saved_url()
    if saved_url:     
        print("Saved URL:", saved_url)
    else:
        while (not saved_url): 
            web_client_app.run()
            print("No URL saved.")
