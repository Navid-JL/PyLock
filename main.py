import threading

lock = threading.Lock()


def modify_shared_data():
    lock.acquire()
    # Code to modify shared data goes here
    lock.release()
