import asyncio

from app.base import BaseAPP
from app.server import Server
from core import LPlayer
from utils import aio


class CliAPP(BaseAPP):
    def __init__(self, player):
        super().__init__(player)

    def run(self):
        server = Server(self, self.cp)
        loop = asyncio.get_event_loop()
        aio.create(server.start_server())
        for i in self._providers:
            aio.create(i.init(self.cp))
        loop.run_forever()


if __name__ == '__main__':
    app = CliAPP(LPlayer())
    app.run()
