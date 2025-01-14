from http.server import SimpleHTTPRequestHandler, HTTPServer
import sys


class EchoHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Write logs to stdout instead of stderr
        log_entry = "[%s] %s\n" % (self.log_date_time_string(), format % args)
        sys.stdout.write(log_entry)

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self._set_headers()
        self.wfile.write(body)


def run(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, EchoHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
