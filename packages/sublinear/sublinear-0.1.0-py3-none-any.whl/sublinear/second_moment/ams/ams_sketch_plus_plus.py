from typing import List
from .ams_sketch_plus import AMSSketchPlus
from math import ceil, log
from statistics import median

class AMSSketchPlusPlus:
    """
    AMS-F2-Estimate++ is an extension of the Alon-Matias-Szegedy algorithm that runs
    multiple instances of the algorithm and returns the median of the results to
    reduce the variance of the estimation.

    The second moment is defined as the sum of the squares of the frequencies 
    of distinct items in the stream.
    """

    def __init__(self, n: int, epsilon: float, delta: float) -> None:
        """
        Initializes the AMSSketchPlusPlus class.

        Parameters
        ----------
        n: int
            Size of the input universe.

        epsilon: float
            Approximation error factor.

        delta: float
            Confidence level for the median.
        """
        self.instances = []
        self.num_instances = ceil(log(1 / delta))
        for _ in range(self.num_instances):
            self.instances.append(AMSSketchPlus(n, epsilon))

    def process_stream(self, stream: List[object]) -> None:
        """
        Executes the AMS-F2-Estimate++ algorithm on a stream (list) of elements.

        Parameters
        ----------
        stream: List[object]
            Stream of objects represented as a list.
        """
        for instance in self.instances:
            instance.process_stream(stream)

    def get_estimate(self) -> int:
        """
        Returns the estimated second moment of the stream using the median of
        the results from the multiple instances.

        Returns
        -------
        int
            Estimated second moment of the stream.
        """
        estimates = [instance.get_estimate() for instance in self.instances]
        return int(median(estimates))
