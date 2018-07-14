from urllib.request import urlopen
import datetime
import threading


def pressure_test():

    for i in range(50):

        global count, mutex
        start_time = datetime.datetime.now()
        url = "http://118.24.32.76/"
        content = urlopen(url)
        status = content.getcode()
        print(status)
        now_time = datetime.datetime.now()
        c_time = now_time - start_time
        print(c_time)
        if mutex.acquire():

            count += 1
            mutex.release()

        print("访问次数%s" % count)

        if status != 200:
            break


if __name__ == '__main__':

    count = 0
    thread = []
    mutex = threading.Lock()
    for j in range(50):

        t = threading.Thread(target=pressure_test)
        thread.append(t)

    for t in thread:

        t.start()
    t.join()
