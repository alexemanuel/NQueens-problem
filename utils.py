import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.time()
        output = func(*args, **kwargs)
        end_time = time.time()

        print(f"Elapsed Time: {end_time - start_time:.4f}s")
        return output

    return wrapper



