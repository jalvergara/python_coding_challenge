import time
import psutil
from functools import wraps
import logging


logging.basicConfig(level=logging.INFO)


def time_execution(func):
    """
    Decorator to measure and print the execution time of a function.

    Args:
        func (callable): The function to measure.

    Returns:
        callable: The wrapped function with timing functionality.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"[INFO] Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper


def memory_usage():
    """
    Measures the current memory usage of the process in megabytes and prints it.

    Returns:
        float: The memory usage in megabytes.
    """
    process = psutil.Process()
    mem_info = process.memory_info()
    mem_usage_mb = mem_info.rss / (1024 * 1024)  # Convert to MB
    logging.info(f"[INFO] Memory usage: {mem_usage_mb:.2f} MB")
    return mem_usage_mb
