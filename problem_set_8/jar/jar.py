class Jar:
    def __init__(self, capacity=12):
        """
        Initialize cookie jar with given capacity
        Initially there are assumed to be no cookie in the jar, size = 0
        """
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        """
        Returns cookies in the jar
        """
        return "🍪"*self.size

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        """
        Withdraw n cookies if available. If not raise ValueError
        """
        if self.size < n:
            raise ValueError("There aren't that many cookies in the jar")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Set non-negative capacity for jar
        """
        if capacity < 0:
            raise ValueError("Capacity can't be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        """
        Add n cookies to the jar so long as there is enough space
        """
        if not 0 <= n <= self.capacity:
            raise ValueError
        self._size = n


if __name__ == "__main__":
    jar = Jar()
    jar.deposit(2)
    print(jar)
