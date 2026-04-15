import http.server
import os

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Clean URLs: /privacy -> privacy.html, /terms -> terms.html, etc.
        path = self.path.split('?')[0].split('#')[0]
        if path != '/' and not os.path.splitext(path)[1]:
            html_path = path.lstrip('/') + '.html'
            if os.path.exists(html_path):
                self.path = '/' + html_path
        super().do_GET()

if __name__ == '__main__':
    server = http.server.HTTPServer(('0.0.0.0', 5000), CleanURLHandler)
    print('Serving on port 5000')
    server.serve_forever()
