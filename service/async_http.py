from tornado import ioloop
from tornado.httpclient import AsyncHTTPClient
from tornado import gen


class AsyncHttp:
    def __init__(self, urls, response_parser):
        self.urls = urls
        self.response_parser = response_parser
        self.http_client = AsyncHTTPClient()

    @gen.coroutine
    def fetch_urls(self):
        waiter = gen.WaitIterator(*[self.http_client.fetch(url) for url in self.urls])

        while not waiter.done():
            try:
                response = yield waiter.next()
                self.response_parser(response)
            except Exception as e:
                print(e)
                continue

    def start(self):
        loop = ioloop.IOLoop.current()
        loop.run_sync(self.fetch_urls)