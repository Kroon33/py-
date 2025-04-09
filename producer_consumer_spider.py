import queue
from blog_spider import *
import time
import random
import threading

def do_craw(url_queue: queue.Queue, result_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = craw(url)
        result_queue.put(html)
        print(threading.current_thread().name, f"craw{url} done", "url_queue.size = ", url_queue.qsize(), "result_queue.size = ", result_queue.qsize())
        time.sleep(random.randint(1, 3))

def do_parse(html_queue, fout):
    while True:
        html = html_queue.get()
        result = parse(html)
        for item in result:
            fout.write(str(result) + '\n')

        print(threading.current_thread().name, f"parse{html} done", "html_queue.size = ", html_queue.qsize())
        time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    for url in urls:
        url_queue.put(url)


    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw_thread-{idx}")
        t.start()

    fout = open("02_data.txt", "w")

    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout), name=f"parse_thread-{idx}")
        t.start()




