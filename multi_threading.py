import threading
import time


def main():

    def thread_func(name, interval):
        for i in range(10):
            print("I'm", name)
            time.sleep(interval)
        print(name, "done")

    pt1 = threading.Thread(target=thread_func, args=("Thread 1", 1))
    pt1.start()

    pt2 = threading.Thread(target=thread_func, args=("Thread 2", 2))
    pt2.start()

    print("All threads started")
    pt1.join()
    print("Main thread joined with Thread 1")
    pt2.join()
    print("Main thread joined with Thread 2")
    print("Main thread done")


if __name__ == '__main__':
    main()
