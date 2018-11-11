async def bounded_fetch(session, sem, url):
    """
    Use session object to perform 'get' request on url
    """
    async with sem, session.get(url) as response:
        return await response.json()
