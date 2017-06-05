from .iview import IView, IViewModel

import asyncio
import websockets
import subprocess
import os


class WebView(IView):
    """
    Web-based browser window.
    """
    def update(self):
        # open internet browser window with JS code here

        page = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'webviewclient.html')
        subprocess.call(['open', page])


class WebViewModel(IViewModel):
    def build(self):
        async def hello(websocket, path):
            # name = await websocket.recv()
            # print("< {}".format(name))
            greeting = "Hello {}!".format("Pavlo")
            await websocket.send(greeting)
            print("> {}".format(greeting))

        start_server = websockets.serve(hello, 'localhost', 5678)

        asyncio.get_event_loop().run_until_complete(start_server)
        # asyncio.get_event_loop().run_forever()
