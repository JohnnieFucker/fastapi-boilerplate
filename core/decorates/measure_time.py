import time
import functools


def measure_time(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)  # 如果函数是异步的，使用 await
        end_time = time.time()
        processing_time = round(end_time - start_time, 2)
        # print(f"Function {func.__name__} took {processing_time} seconds to complete.")
        return result, processing_time

    return wrapper
