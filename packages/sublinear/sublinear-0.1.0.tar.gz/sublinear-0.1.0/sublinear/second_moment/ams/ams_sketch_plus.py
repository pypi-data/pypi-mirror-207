from typing import List
from sublinear.utils.hash_generator import HashGenerator
from math import ceil

class AMSSketchPlus:
    """
    AMS-F2-Estimate (also known as the Alon-Matias-Szegedy algorithm) is a 
    streaming algorithm for estimating the second moment of a data stream.

    The second moment is defined as the sum of the squares of the frequencies 
    of distinct items in the stream.

    The algorithm is based on maintaining counters 'z' that are updated
    according to their corresponding random hash functions.
    """

    def __init__(self, n: int, epsilon: float) -> None:
        """
        Initializes the AMS-F2-Estimate class.

        Parameters
        ----------
        n: int
            Size of the input universe.

        epsilon: float
            Approximation error factor.
        """
        self.n = n
        self.k = ceil(18 / epsilon)

        self.z = [0 for _ in range(self.k)]
        self.y = [HashGenerator(self.n, k=4, m=2).generate_hash_function() for _ in range(self.k)]

    def process_stream(self, stream: List[object]) -> None:
        """
        Executes the AMS-F2-Estimate algorithm on a stream (list) of elements.

        Parameters
        ----------
        stream: List[object]
            Stream of objects represented as a list.
        """
        for a_j in stream:
            self.z = [self.z[i] + (-1 if self.y[i].hash_integer(a_j) == 0 else 1) for i in range(self.k)]
            

    def get_estimate(self) -> int:
        """
        Returns the estimated second moment of the stream.

        Returns
        -------
        int
            Estimated second moment of the stream.
        """
        return int(sum(map(lambda x: x**2, self.z)) / self.k)