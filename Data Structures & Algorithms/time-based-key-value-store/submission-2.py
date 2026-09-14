import bisect

class TimeMap:

    def __init__(self):
        self.data: dict[list[tuple[str, int]]] = {} # Stores in the format (value, timestamp) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        l = self.data.get(key, None)

        if l is None:
            self.data[key] = [(value, timestamp)]
            return 
        
        bisect.insort(l, (value, timestamp), key=lambda r: r[1])

    def get(self, key: str, timestamp: int) -> str:
        values = self.data.get(key, None)

        if values is None:
            return ""

        idx = bisect.bisect(values, timestamp, key=lambda r: r[1])

        if idx == 0:
            return ""

        return values[idx - 1][0]

        

        







        
