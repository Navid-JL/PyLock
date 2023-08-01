import threading

lock = threading.Lock()

shared_data = []


def modify_shared_data():
    with lock:
        shared_data.append("New data")


def main():
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=modify_shared_data)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    with lock:
        print(shared_data)


if __name__ == "__main__":
    main()
