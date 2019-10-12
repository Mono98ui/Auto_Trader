from concurrent.futures import ThreadPoolExecutor as PoolExecutor


class WorkerGenerator:

    def __init__(self):
        pass

    def assign_worker(self, function, value_list):
        with PoolExecutor(max_workers=6) as executor:
            for _ in executor.map(function, value_list):
                pass
