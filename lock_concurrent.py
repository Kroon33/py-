import threading
import time

class Account:
    def __init__(self, balance=0):
        self.balance = balance


lock = threading.Lock()


def draw(account, amount):
    with lock:
        if account.balance >= amount:
            time.sleep(0.5)
            print(threading.current_thread().name, "取钱成功")
            account.balance -= amount
            print(threading.current_thread().name, "余额为:", account.balance)

        else: 
            print(threading.current_thread().name, "余额不足")
            print(threading.current_thread().name, "余额为:", account.balance)


if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(target=draw, args=(account, 800), name="线程A")
    tb = threading.Thread(target=draw, args=(account, 800), name="线程B")

    ta.start()
    tb.start()

