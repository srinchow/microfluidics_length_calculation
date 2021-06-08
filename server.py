import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options

from Microfluidics_Length import *

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", IndexHandler), (r"/upload", UploadHandler)]
        tornado.web.Application.__init__(self, handlers)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("upload_form.html")


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        file1 = self.request.files["file1"][0]
        original_fname = file1["filename"]
        extension = os.path.splitext(original_fname)[1]
        fname = "".join(
            random.choice(string.ascii_lowercase + string.digits) for x in range(6)
        )
        final_filename = fname + extension
        output_file = open("images/" + final_filename, "wb")
        output_file.write(file1["body"])
        data = action(final_filename)
        data = data * 6
        data = format(data, ".4f")
        self.finish(str(data) + " cm")


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()