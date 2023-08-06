from typing import List
from .morris_basic import MorrisCounter

class MorrisPlusCounter:
    """
    Morris Plus Counter is an extension of the Morris Counter that runs multiple
    Morris Counters in parallel and outputs the average of the estimates. This
    improves the accuracy of the count estimate.

    Attributes
    ----------
    s : int
        Number of Morris Counters.
    counters : List[MorrisCounter]
        List of Morris Counters.
    """

    def __init__(self, s: int):
        """
        Initializes Morris Plus Counter.

        Parameters
        ----------
        s : int
            Number of Morris Counters.
        """
        self.s = s
        self.counters = [MorrisCounter() for _ in range(s)]

    def process_stream(self, stream: List[int]) -> None:
        """
        Processes the input data stream with the Morris Plus Counter algorithm.

        Parameters
        ----------
        stream : List[int]
            Data stream represented as a list of integers.
        """
        for item in stream:
            for counter in self.counters:
                counter.process()

    def estimate_count(self) -> int:
        """
        Estimates the count of the elements in the data stream.

        Returns
        -------
        int
            Estimated count of elements in the data stream.
        """
        estimates = [counter.estimate_count() for counter in self.counters]
        return int(sum(estimates) / self.s)
