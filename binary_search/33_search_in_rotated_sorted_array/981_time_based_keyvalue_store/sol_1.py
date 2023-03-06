class TimeMap:

    def __init__(self):
        # 1) - We initialize the with a hash map to store the values.
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 2) - For storing the values we first check if the key is not in the
        # store, if is not we initialize that key with an empty array.

        # 3) - Then we append the value as a two element array, the first
        # position containing the value, and the other position containing the
        # timestamp.
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # 5) - Then for the get method we return empty strings as specified
        # in the prompt is the key is not on the store.

        # 6) - If the key IS in the store we are going to return the most
        # recent one based on the timestamp provided thats why we are using
        # a binary search.

        # 7) - If arr[m][1] is less than the timestamp provided we
        # update our return value and we update our left pointer to see
        # if we have more arr[m][1] values that are greater than our current
        # return value and less than the given timestamp.

        # 8) - Otherwise we update our right pointer.
        if key not in self.store:
            return ""
        else:
            l,r = 0, len(self.store[key]) - 1
            arr = self.store[key]
            value = ""
            while l <= r:
                m = (l+r)//2
                if arr[m][1] <= timestamp:
                    value = arr[m][0]
                    l = m + 1
                else:
                    r = m - 1
            return value