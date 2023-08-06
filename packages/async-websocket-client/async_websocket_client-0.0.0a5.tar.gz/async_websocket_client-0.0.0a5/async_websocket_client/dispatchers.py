from __future__ import annotations

import logging
import random
from typing import Any

from websockets.client import WebSocketClientProtocol

# from sdk.client import BaseDispatcher


logger = logging.getLogger('async_websocket_client')


class BaseDispatcher(object):

    app: Any
    ws: WebSocketClientProtocol

    def set_app(self, app: Any):
        self.app = app

    async def set_websocket(self, ws: WebSocketClientProtocol):
        self.ws = ws
        self.tasks = getattr(self, 'tasks', [])

    async def before_connect(self):
        logger.info('before_connect')

    async def on_connect(self):
        logger.error('on_connect')
        await self.ws.send('bot on_connect')

    async def before_disconnect(self):
        logger.info('before_disconnect')

    async def on_disconnect(self):
        logger.info('on_disconnect')

    async def on_message(self, message: str):
        logger.error(f'client | on_message: {message}')

        if message == 'ping':
            await self.ws.send('pong')
            return

        try:
            await self.ws.send(str(int(message) + 1))

        except Exception:
            await self.ws.send('-1111111')

    async def make_message(self):
        return str(random.randint(1, 100))
