import threading

lock = threading.Lock()

shared_data = []


def modify_shared_data():
    with lock:
        shared_data.append("New data")
