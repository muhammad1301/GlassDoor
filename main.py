from scraper import Glassdoor
import threading
import time

HEADLESS = False
num_threads = 1

def main():

    G = Glassdoor('uc', headless2=HEADLESS, start=True)
    # G.open_web()
    start_time = time.time()
    G.login()
    time.sleep(5)
    # G.open_links()
    G.open_links_2()
    end_time = time.time()
    execution_time = end_time - start_time
    print(execution_time)


if __name__ == '__main__':
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=main)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
