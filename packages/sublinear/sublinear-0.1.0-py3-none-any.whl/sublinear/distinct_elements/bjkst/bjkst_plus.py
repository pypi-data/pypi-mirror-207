from typing import List
from .bjkst_sketch import BJKSTSketch
from math import ceil, log
import statistics

class BJKSTSketchPlus:
    """
    The BJKST sketch with epsilon-delta approximation is a probabilistic data structure
    that serves as a distinct element counter in a stream of data.

    This implementation runs multiple instances of the BJKST algorithm and returns the
    median of the estimates to improve the accuracy of the estimation.
    """

    def __init__(self, n: int, epsilon: float, delta: float, b: float = 10, max_input_length: int = 64, c: float = 576):
        """
        Initializes BJKSTSketchPlus class.

        Parameters
        ----------
        Initializes BJKST Sketch class.

        Parameters
        ----------
        n: int
            Size of the input universe.

        b: float
            Constant factor for controlling the hash function range of g.

        c: float
            Constant factor for size of set B.

        epsilon: float
            Approximation error factor.

        delta: float
            Confidence level.

        max_input_length: int, optional
            Maximum length of the input elements, used for generating hash functions.
        """
        self.instances = []
        self.num_instances = ceil(log(1 / delta))
        for _ in range(self.num_instances):
            self.instances.append(BJKSTSketch(n, epsilon, b, max_input_length=max_input_length, c=c))

    def process_stream(self, stream: List[object]) -> None:
        """
        Executes the BJKST algorithm with epsilon-delta approximation on a stream (list) of elements.

        Parameters
        ----------
        stream: List[object]
            Stream of objects represented as a list.
        """
        for instance in self.instances:
            instance.process_stream(stream)

    def estimate_distinct_elements(self) -> int:
        """
        Returns the estimated number of distinct elements in the stream using the median of
        the results from the multiple instances.

        Returns
        -------
        int
            Estimated number of distinct elements.
        """
        estimates = [instance.estimate_distinct_elements() for instance in self.instances]
        return int(statistics.median(estimates))
