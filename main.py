import threading

lock = threading.Lock()

shared_data = []


def modify_shared_data():
    lock.acquire()
    shared_data.append("New data")
    lock.release()
