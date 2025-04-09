## CPU密集型计算 CPU-bound

程序运算受到CPU性能的限制，IO在很短的时间内就可以完成，但是CPU需要大量的计算和处理



## IO密集型计算 I/O-bound

程序运算受到IO限制，大部分时间CPU都在等待IO的读写操作，CPU占用低



一个进程中可以启动多个线程，一个线程中可以启动多个协程



### 多线程Thread

相比起进程，占用的资源更少，但是只能够并发执行，不可以利用多个CPU

适用于IO密集型计算，同时运行的任务数目要求不多

### 多进程Process

可以使用多核CPU进行并行运算，占用的资源最多

适用于CPU密集型计算

### 多协程Coroutine

内存开销最少，启动协程数量最多，代码实现复杂

适用于IO密集型计算，需要超多任务运行



## 全局解释器锁GIL

python解释器用于同步线程的一种机制，它可以是的任何时刻仅有一个线程在执行



## 创建多线程的方法

```python
1.准备一个函数
def my_func(a, b):
    do_craw(a, b)
2.创建一个线程
import threading
t = threading.Thread(target = my_func, args = (100, 200))
3.启动线程
t.start()
4.等待结束
t.join()
```

## 多线程数据通信queue.Queue

```python
import queue
q = queue.Queue()
q.put(item)//添加元素
item = q.get()//获取元素


q.qsize()//判断元素多少
q.empty()//判断是否为空
q.full()//判断是否已满
```





## 线程安全问题和lock

由于线程的执行随时会发生切换，就造成了不可预料的结果，出现线程不安全

### lock由于解决线程安全

1.try-finally模式

```python
import threading
lock = threading.Lock()
lock.acquire() # 获取锁 -》 执行代码 -》 释放锁
try:
    # do sth
finally:
    lock.release()
```

2.with模式

```
import threading
lock = threading.Lock()
with lock:
	# do sth
```

## 线程池

新建线程系统需要分配资源，终止线程系统需要回收资源，如果可以重用线程，就可以减去新建/终止的开销

### 好处

1.提升性能：因为减去了大量的新建，终止线程的开销，重用了线程资源

2.适用场景：适合处理突发性的大量请求或需要大量线程完成任务，但实际任务处理时间较短

3.防御功能：有效避免系统因为创建线程过多，从而导致系统负荷过大相应变慢的问题

### 线程池方法

`from concurrent.futures import ThreadPoolExecutor, as_completed`

1.使用map函数

```python
with ThreadPoolExecutor() as pool:
	results = pool.map(craw, urls)
    
    for result in results:
        print(result)
```

2.future方法

```python
with ThreadPoolExecutor() as pool:
    futures = [ pool.submit(craw, url) for url in urls]
    
    for future in futures:
        print(futures.result())
    for future in as_completed(futures): #这种方法顺序不定
        print(future.result())
```

