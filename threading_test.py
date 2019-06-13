import threading
import time
def target():
    print("the current threading %s is runing"
       %(threading.current_thread().name))
    time.sleep(1)
    print("the current threading %s is ended"%(threading.current_thread().name))

print("the current threading %s is runing"%(threading.current_thread().name))
## 属于线程t的部分
t = threading.Thread(target=target)
t.start()
## 属于线程t的部分
t.join() # join是阻塞当前线程(此处的当前线程时主线程) 主线程直到Thread-1结束之后才结束
print("the current threading %s is ended"%(threading.current_thread().name))