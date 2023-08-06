import time

def time_spended(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Spended time: {str(end - start)[:4]} seconds')
        return result
    return wrapper
