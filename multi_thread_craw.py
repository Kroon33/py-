from blog_spider import *
import threading
import time


urls = [f"https://www.cnblogs.com/#p{i}" for i in range(1,50)]

def single_thread():
    start_time = time.time()   
    for url in urls:
        craw(url)
    end_time = time.time()
    print("Single thread time:", end_time - start_time)

def multi_thread():
    start_time = time.time()
    threads = []

    for url in urls:
        threads.append(threading.Thread(target = craw, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print("Multi thread time:", end_time - start_time)

if __name__ == "__main__":
    single_thread()
    multi_thread()