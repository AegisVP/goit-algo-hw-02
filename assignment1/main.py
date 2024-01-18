from queue import Queue

queue = Queue()


def generate_request():
    request = 'new request'
    queue.put(request)

    print('New request generated')
    print(f"{queue.qsize()} equests in queue")


def process_request():
    if (queue.qsize() > 0):
        processed_request = queue.get()
        print(f"Removed request from queue: {processed_request}")
        print(f"{queue.qsize()} requests in queue")
    else:
        print('Queue is empty')


if __name__ == '__main__':
    while True:
        generate_request()
        process_request()
