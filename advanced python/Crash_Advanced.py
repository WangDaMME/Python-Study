'''
1️⃣ Python 并发三种方式

Python 常见并发模型：

类型	适合场景	特点
多线程 threading	IO密集	共享内存
多进程 multiprocessing	CPU密集	绕过GIL （GIL = Global Interpreter Lock 意思是： 同一时间只能有 一个线程执行 Python 字节码）
协程 asyncio	高并发IO	单线程
'''
import threading

'''


#1. 多线程 threading
import time
def task():
    for i in range(3):
        print("task running")
        time.sleep(1)
#如果 单线程执行：task running (1s) task running (1s) task running
t = threading.Thread(target=task) # 创建一个 线程对象 t， 让这个线程 执行 task 函数， 新线程 -> 执行 task()
t.start() # 启动线程。 此时程序变成： 主线程 (main thread) 新线程 (t)

print("main thread") # 主线程打印完了 后续 还能看到 t.结果

'''
#lock = threading.Lock()  - 互斥锁 (Mutex) synchronized / ReentrantLock

count = 0
lock = threading.Lock()

def add():
    global count
    for i in range(100000):
        lock.acquire() # with lock:
        count += 1
        lock.release()

threads = []

for i in range(5):
    t = threading.Thread(target=add)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(count)
# 理论5000， 但可能变成： 4723


# 有 lock atomic volatile 这些关键字吗

'''
#2. 多进程 multiprocessing
每个 Process 是独立进程
'''
from multiprocessing import Process
import os
def task():
    print("task running in: ", os.getpid())

if __name__ == '__main__':
    p1 = Process(target=task)
    p2 = Process(target=task)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("main thread")

# running in process 12345
# running in process 12346
# main process done


'''
3. 协程 coroutine
协程是 用户态线程， 单线程 任务主动切换； 👉 比线程更轻量的一种“并发任务”，由程序自己控制什么时候暂停、什么时候继续执行。
协程 = 可以主动暂停和恢复的函数 -
【Python 用 async / await】- asyncio
假设你有两个任务：

任务A：下载网页
任务B：读取文件
1）如果用普通函数：A执行完 → B执行
2）如果用线程：
线程A
线程B
（操作系统调度） -- 线程 创建成本高，上下文切换慢

3）所以出现 协程：
A执行一会 → 暂停
B执行一会 → 暂停
A继续执行-程序自己控制切换。
'''
import asyncio
async def task1():
    print("task 1 start")
    await asyncio.sleep(2)
    print("task 1 end")

async def task2():
    print("task 2 start")
    await asyncio.sleep(1)
    print("task 2 end")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# 输出：
#
# task1 start
# task2 start
# task2 end
# task1 end
#
# 说明：
#
# task1 等待 2s
# task2 等待 1s
#
# 但 两个任务是同时运行的。

'''
协程运行方式
task1 start
await sleep(2)
      ↓
任务暂停
      ↓
task2 start
await sleep(1)
      ↓
task2 end
      ↓
task1 resume
task1 end

'''
