class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("capacity must be >= 0")
        self.capacity = capacity
        self._tmp = {}  # временно, потом заменим на DLL + custom HashMap

    def get(self, key: int):
        return self._tmp.get(key, -1)

    def put(self, key: int, value: int):
        if self.capacity == 0:
            return
        # временно без eviction — это только для старта
        self._tmp[key] = value