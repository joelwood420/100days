import time


def start():
    """Return a high-resolution start timestamp."""
    return time.perf_counter()


def stop():
    """Return a high-resolution stop timestamp."""
    return time.perf_counter()


def elapsed(start_time, end_time):
    """Return elapsed seconds between start_time and end_time."""
    return end_time - start_time
