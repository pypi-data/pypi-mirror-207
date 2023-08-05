# async-rotating-proxy
Run an API on your local machine that reroutes traffic through rotating proxies.

- Excellent for scaling your web scraping
- Designed for page-by-page dynamic proxy switching with pyppeteer

## Installation
`pip install async_rotating_proxy`

## Usage
```py
from async_rotating_proxy import ProxyAPI
import pyppeteer

proxies = [
  ip:port,
  ip:port,
  ip:port
]

with ProxyAPI(proxies) as api:
  url = api.format_url("http://checkip.dyndns.org")

  browser = await pyppeteer.launch()
  page = await browser.newPage()
  await page.goto(url)
```


## Purpose
The article referenced below sums it up pretty well:
"The chrome browser does not support fain-grained proxy configuration out of the box. Therefore, the following use cases are not possible when using puppeteer in combination with Google Chrome:

    Using different proxies for different tabs/windows
    Switching proxies without restarting the browser

This is a bit annoying, because restarting the entire browser is an expensive operation in terms of computational resources. The chrome restart takes up to two seconds (depending on the system). We ideally want to switch proxies whenever the need arises without restarting the entire chrome process. This is a common requirement when scraping websites in scale."

## Reference
https://incolumitas.com/2020/12/20/dynamically-changing-puppeteer-proxies/
