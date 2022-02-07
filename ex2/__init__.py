from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        def decorator(*args, **kwargs):
            total_time = 0
            for i in range(num):
                start_time = time.time()
                func(*args, **kwargs)
                lead_time = time.time() - start_time
                total_time += lead_time
                print(f'Время выполнения: {lead_time}')
            print(f'Cреднее время: {total_time / num}\n')
        return decorator
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
