import asyncio


def create(cor):
    loop = asyncio.get_event_loop()
    loop.create_task(cor)
