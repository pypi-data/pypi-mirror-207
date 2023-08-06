import math
import numpy as np
from typing import List

from .morris_plus import MorrisPlusCounter

class MorrisPlusPlusCounter:
    """
    Morris Plus Plus Counter is an extension of the Morris Plus Counter that
    runs multiple Morris Plus Counters in parallel and outputs the median of
    the estimates. This improves the accuracy of the count estimate further.

    Attributes
    ----------
    s : int
        Number of Morris Counters in each Morris Plus Counter.
    t : int
        Number of Morris Plus Counters.
    counters : List[MorrisPlusCounter]
        List of Morris Plus Counters.
    """

    def __init__(self, epsilon: float, delta: float):
        """
        Initializes Morris Plus Plus Counter.

        Parameters
        ----------
        epsilon : float
            Error factor.
        delta : float
            Confidence factor.
        """
        self.s = int(math.ceil(1 / (epsilon ** 2)))
        self.t = int(math.ceil(math.log(1 / delta)))
        self.counters = [MorrisPlusCounter(self.s) for _ in range(self.t)]

    def process_stream(self, stream: List[int]) -> None:
        """
        Processes the input data stream with the Morris Plus Plus Counter algorithm.

        Parameters
        ----------
        stream : List[int]
            Data stream represented as a list of integers.
        """
        for item in stream:
            for counter in self.counters:
                counter.process_stream([item])

    def estimate_count(self) -> int:
        """
        Estimates the count of the elements in the data stream.

        Returns
        -------
        int
            Estimated count of elements in the data stream.
        """
        estimates = [counter.estimate_count() for counter in self.counters]
        return int(np.median(estimates))