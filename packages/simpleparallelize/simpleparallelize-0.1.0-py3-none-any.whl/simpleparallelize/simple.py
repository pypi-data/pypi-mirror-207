from tqdm import tqdm
import multiprocessing as mp
import threading
from functools import partial

def init_progress_bar(shared_value):
    global shared_progress
    shared_progress = shared_value


def update_progress_bar(pbar, shared_progress):
    while not pbar.n >= pbar.total:
        with shared_progress.get_lock():
            current_progress = shared_progress.value
            pbar.update(current_progress - pbar.n)


def wrapper_request(request, func):
    response = func(request)
    with shared_progress.get_lock():
        shared_progress.value += 1
    return response

def mp_progress_bar(requests, func):
    shared_progress = mp.Value("i", 0)
    with mp.Pool(processes=mp.cpu_count(), initializer=init_progress_bar, initargs=(shared_progress,)) as pool:
        with tqdm(total=len(requests), desc="Processing requests", ncols=100) as pbar:
            update_thread = threading.Thread(target=update_progress_bar, args=(pbar, shared_progress))
            update_thread.start()
            partial_func = partial(wrapper_request, func=func)
            responses = pool.map(partial_func, requests)
            update_thread.join()

    return responses

def run_requests(requests, func):
    return mp_progress_bar(requests, func)