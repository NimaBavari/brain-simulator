import asyncio
import base64
import datetime

import websockets

from config import (DECAY_DIFF_PER_SEC, OUTPUT_WEBSOCKET_HOST, OUTPUT_WEBSOCKET_PORT,
                    RADIUS_REL_SIZE)
from src import event_feeder, freq_feeder, redis_client


async def autostore(t, freq, event):
    dataload = base64.b64encode(
        str({"time": t, "freq": freq, "event": event}).encode("ascii"))
    redis_client.lpush("store", dataload)


async def autoload(t, freq):
    for mem_in_base64 in redis_client.lrange("store", 0, -1):
        mem = eval(base64.b64decode(mem_in_base64).decode("ascii"))
        freq_in_past = freq / (1 - DECAY_DIFF_PER_SEC)**(t - mem["time"])
        if 1 - RADIUS_REL_SIZE < mem["freq"] / freq_in_past < 1 + RADIUS_REL_SIZE:
            return {k: v for k, v in mem.items() if k != "freq"}
    return {"time": 0, "event": 0}


async def mainloop(ws_protocol):
    while True:
        freq = next(freq_feeder())
        event = next(event_feeder())
        current_time = datetime.datetime.now().timestamp()
        await autostore(current_time, freq, event)
        output = await autoload(current_time, freq)
        await ws_protocol.send(str(output))


async def serve():
    async with websockets.serve(mainloop, OUTPUT_WEBSOCKET_HOST, OUTPUT_WEBSOCKET_PORT):
        print("Websocket at ws://%s:%s started serving." %
              (OUTPUT_WEBSOCKET_HOST, OUTPUT_WEBSOCKET_PORT))
        await asyncio.Future()
    print("Websocket closed.")

if __name__ == "__main__":
    asyncio.run(serve())
