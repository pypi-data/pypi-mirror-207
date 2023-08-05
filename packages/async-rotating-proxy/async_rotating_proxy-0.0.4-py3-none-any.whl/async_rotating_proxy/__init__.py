from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
import uvicorn

from fake_headers import Headers

import aiohttp
from multiprocessing import Process

import urllib.parse
import random
import os


def app(proxies: list[str],
        proxy_username: str | None = None, 
        proxy_password: str | None = None,
        proxy_scheme: str = "http",
        fake_headers: bool = True
        ):
    """Create a FastAPI instance which routes GET requests through proxies.

    Args:
        proxies (list[str]): List of proxies to route traffic through in format ip:port
        username (str | None): Username for authentication if any
        password: (str | None): Password for authenticaiton if any
        schemes: (tuple[str]): URI schemes for proxies (http, https, socks5)
        fake_headers (bool): Generate fake headers for requests

    Returns:
        FastAPI: The proxy-redirect server
    """

    app = FastAPI()

    app.pid = os.getpid()

    @app.get("/")
    async def forward_proxy(request: Request, url: str):
        """Forward a request through a proxy and return the response

        Args:
            url (str): URL to get encoded with urllib.parse.quote_plus()

        Returns:
            HTMLResponse: The requested page obtained through proxy
        """
        # Decode url
        url = urllib.parse.unquote_plus(url)

        # Randomly select proxy
        proxy = random.choice(proxies)
        
        # Build proxy URL
        if proxy_username and proxy_password:
            proxy = f"{proxy_scheme}://{proxy_username}:{proxy_password}@{proxy}"
        else:
            proxy = f"{proxy_scheme}://{proxy}"

        # Get the page and return HTML response
        async with aiohttp.ClientSession() as session:
            headers = Headers(headers=True).generate() if fake_headers else {}

            async with session.get(url, proxy=proxy, headers=headers) as response:
                html = await response.content.read()
                return HTMLResponse(html.decode())

    return app


class ProxyAPI():
    """Start an API on localhost to redirect traffic through proxies

    Usage:
        with ProxyAPI([proxy_list]) as proxy_api:
            url = proxy_api.format_url("your_url")
            do scraping stuff with your url now
        

    Constructor Args:
        proxies (list[str]): List of proxies to rotate through in ip:port form
        proxy_username (str | None): Username for proxy authentication if applicable
        proxy_password (str | None): Password for proxy authentication if applicable
        port (int): The port on localhost where the proxy API is running
        proxy_scheme (http): The scheme of the proxy server
        fake_headers (bool): Set fake headers on each request
    """
    api_pid: int

    def __init__(
            self,
            proxies: list[str], 
            proxy_username: str | None = None,
            proxy_password: str | None = None,
            port: int = 8000,
            proxy_scheme: str = "http",
            fake_headers: bool = True
        ):
        self.proxies = proxies
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password
        self.port = port
        self.proxy_scheme = proxy_scheme
        self.fake_headers = fake_headers


    def __enter__(self):
        self._process = Process(target=self._start_server)
        self._process.start()
        return self
        
    
    def __exit__(self, exc_type, value, traceback):
        self._process.terminate()


    def _start_server(self):
        """Start a FastAPI daemon for routing requests through proxies."""
        api = app(self.proxies, 
                  proxy_username=self.proxy_username,
                  proxy_password=self.proxy_password,
                  proxy_scheme=self.proxy_scheme,
                  fake_headers=self.fake_headers)

        uvicorn.run(api, port=self.port)


    def format_url(self, url: str):
        """Format the URL to route through the ProxyAPI server.
    
        1. Encodes the URL parameter
        2. Prepends http://127.0.0.1:{port}/ to the URL

        Args:
            url (str): URL to format

        Returns:
            str: URL which will route through the ProxyAPI
        """
        encoding = urllib.parse.quote_plus(url)
        return f"http://127.0.0.1:{self.port}/?url={encoding}"
