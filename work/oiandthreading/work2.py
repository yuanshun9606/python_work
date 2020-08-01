import threading


def tread_job():
    print('This is an added Thread , number is %s' % threading.current_thread())


def main():
    added_thread = threading.Thread(target=tread_job)
    added_thread.start()


if __name__ == '__main__':
    main()
