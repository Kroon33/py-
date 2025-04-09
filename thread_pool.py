

import concurrent.futures
from blog_spider import *

with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(craw, urls)
    htmls = list(zip(urls, htmls))
    for url, html in htmls:
        print(url, len(html))
print("done")

with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(parse, html)
        futures[future] = url
        print(url, len(html))

    for future, url in futures.items():
        result = future.result()
        print(url, result)