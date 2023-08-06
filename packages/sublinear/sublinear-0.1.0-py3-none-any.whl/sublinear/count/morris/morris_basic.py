import random
from typing import List

class MorrisCounter:
    """
    Morris Counter is a probabilistic counter for counting elements in a stream
    using logarithmic space. The algorithm was proposed by Robert Morris in 1978.

    Attributes
    ----------
    c : int
        Counter value.
    """

    def __init__(self):
        """
        Initializes Morris Counter.
        """
        self.c = 0

    def process_stream(self, stream: List[int]) -> None:
        """
        Processes the input data stream with the Morris Counter algorithm.

        Parameters
        ----------
        stream : List[int]
            Data stream represented as a list of integers.
        """
        for item in stream:
            self.process()

    def process(self) -> None:
        """
        Updates the counter value with probability 1/(2^c).
        """
        if random.random() < 1 / (2 ** self.c):
            self.c += 1

    def estimate_count(self) -> int:
        """
        Estimates the count of the elements in the data stream.

        Returns
        -------
        int
            Estimated count of elements in the data stream.
        """
        return (2 ** self.c) - 1