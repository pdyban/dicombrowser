from .iview import IView, IViewModel

import asyncio
import websockets
import subprocess
import os
from .model import Model
import json
from collections import OrderedDict


class WebView(IView):
    """
    Web-based browser window.
    """
    def __init__(self, address, port):
        super(WebView, self).__init__()
        self.address = address
        self.port = port

    def update(self):
        # open internet browser window with JS code here

        page = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'webviewclient.html')
        subprocess.call(['open', page])


class WebViewModel(IViewModel):
    def __init__(self, model, view):
        super(WebViewModel, self).__init__(model=model, view=view)
        self.address = view.address
        self.port = view.port
        self.json_str = ''

    def build(self):
        print('Building WebViewModel')

        items = []
        if self.model is not None and self.model.items is not None:
            for fname, tree in self.model.items.items():
                line = OrderedDict()
                line['Filename'] = fname
                for key, value in tree.items():
                    line[key] = value

                items.append(line)

                self.json_str = json.dumps(items)
                print('Composed JSON string: ' + self.json_str)

    async def hello(self, websocket, path):
        while True:
            print('Processing incoming message on server')
            arg = await websocket.recv()
            print('Message on server: ' + arg)

            self.model = Model(arg, self.model.select_tags)
            self.model.viewmodels.append(self)
            print('Found %d items' % (len(self.model.items)))

            self.build()

            # await websocket.send('clear')
            await websocket.send(self.json_str)
            # for line in self.items:
            #    await websocket.send(line)

            print('Finish')

    def start_server(self):
        start_server_async_function = websockets.serve(self.hello, self.address, self.port)
        asyncio.get_event_loop().run_until_complete(start_server_async_function)
        print('Started server')

    def run_forever(self):
        loop = asyncio.get_event_loop()
        loop.run_forever()
        print("Eternal loop interrupted")
