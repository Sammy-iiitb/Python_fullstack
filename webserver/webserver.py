from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#common gateway interface library
import cgi

# below is the function overriding of the base function do_get
# in webserverhandler class which has do_Get and do_post functions in it
class WebServerHandler(BaseHTTPRequestHandler):
    # do_get function handles the get requests by the user and sends the
    # response 200 or similar for the respective query of the user
    def do_GET(self):
        # this function tells what to do on a get request
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1>Hello!</h1>"
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
            return

        if self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1>&#161 Hola !</h1>"
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
            return
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            # when server receive a post request below code indicates a successful post
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # cgi parser header function parses an html form header into
            # main value dictionary of parameters liek json and then uses
            # multipart function to colelct entries of a form and then get
            # specific field and store them in an array
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields= cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')


            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this:</h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass
    # there are two functions in this file main and handler
    # main tells the port on which the server is running
    # handler function handles the requests of the client machine
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server running on port %s" % port
        # serve_forever function constantly listen on the port
        server.serve_forever()
    except KeyboardInterrupt:
        # if ctrl + c is pressed by the user then calls this exception
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
