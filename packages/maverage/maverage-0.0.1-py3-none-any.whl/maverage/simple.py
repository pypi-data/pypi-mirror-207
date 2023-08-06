"""Implements the Simple Moving Average."""
# For math behind the Simple Moving Average, refer to
# https://en.wikipedia.org/wiki/Moving_average#Simple_moving_average

from collections import deque


class Simple:
    """Simple Moving Average"""
    def __init__(self, size) -> None:
        if not (isinstance(size, int) and size > 0):
            raise ValueError(f'`size` must be a positive integer (not {size})')
        self._deque = deque([])
        self._cumulative = 0

        self._samples = 0
        self._size = size

    def input(self, value) -> 'Simple':
        """Input next value. Do not calculate the average."""
        if self._samples < self._size:
            self._cumulative += value
            self._samples += 1
            self._deque.appendleft(value)
        else:
            old_value = self._deque.pop()
            self._cumulative += value - old_value
            self._deque.appendleft(value)
        return self

    @property
    def average(self) -> float:
        """Get the current average of the internal data."""
        return self._cumulative / self._samples
