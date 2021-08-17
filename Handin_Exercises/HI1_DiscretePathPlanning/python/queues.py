"""Simple implementation of FIFO, LIFO, and PriorityQueue."""

import heapq


class FIFO:
    """FIFO queue."""

    q = []

    def __init__(self):
        """Init queue."""
        self.q = []

    def insert(self, x):
        """Insert object into queue."""
        self.q.append(x)

    def pop(self):
        """Get object from queue."""
        return self.q.pop(0)

    def IsEmpty(self):
        """Test if queue is empty."""
        return len(self.q) == 0

    def size(self):
        """Return size of queue."""
        return len(self.q)

    def peek(self):
        """Peek into queue."""
        return self.q[0]


class LIFO(FIFO):
    """LIFO queue."""

    def insert(self, x):
        """Insert object into LIFO."""
        self.q.insert(0, x)


class PriorityQueue(FIFO):
    """Priority queue."""

    def insert(self, priority, x):
        """Insert prioritized object into queue.

        obj.insert(priority, x) - Insert object x with priority priority.
        """
        heapq.heappush(self.q, (priority, x))

    def update_key(self, priority, x):
        """Update priority of key already in queue.

        obj.update_key(priority, x) - Update priority of object x to new priority priority.
        """
        self.q = [(prio, key) if key != x else (priority, x) for (prio, key) in self.q]
        heapq.heapify(self.q)

    def pop(self):
        """Pop value from queue with lowest priority.

        Returns pair (priority, object)
        """
        return heapq.heappop(self.q)

    def ismember(self, x):
        return x in [key for _, key in self.q]
