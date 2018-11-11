from sanic import Sanic
from sanic.response import json

from routes import services
from docs import add_swagger

import asyncio
import aiohttp

app = add_swagger(Sanic(__name__))

sem = None

@app.listener('before_server_start')
def init(sanic, loop):
    global sem
    concurrency_per_worker = 4
    sem = asyncio.Semaphore(concurrency_per_worker, loop=loop)


@app.route("/")
async def test(request):
    """
    Download and serve example JSON
    """
    url = "https://api.github.com/repos/channelcat/sanic"

    async with aiohttp.ClientSession() as session:
        sanic_response =  services.bounded_fetch(session, sem, url)

        reddit_url = 'https://www.reddit.com/r/python/top.json?sort=top&t=day&limit=5'
        py_response = services.bounded_fetch(session, sem, reddit_url)

        ds_url = 'https://www.reddit.com/r/datascience/top.json?sort=top&t=day&limit=5'
        ds_response = services.bounded_fetch(session, sem, ds_url)

        results = await asyncio.gather(sanic_response, py_response, ds_response)

        res = {}
        res['sanic'], res['python'], res['dsa'] = results

        return json(res)


app.run(host="0.0.0.0", port=8000, workers=4, auto_reload=True, debug=True)
