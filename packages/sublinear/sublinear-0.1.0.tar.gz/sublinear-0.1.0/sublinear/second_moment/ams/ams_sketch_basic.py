from typing import List
from sublinear.utils.hash_generator import HashGenerator

class AMSSketchBasic:
    """
    AMS-F2-Estimate (also known as the Alon-Matias-Szegedy algorithm) is a 
    streaming algorithm for estimating the second moment of a data stream.

    The second moment is defined as the sum of the squares of the frequencies 
    of distinct items in the stream.

    The algorithm is based on maintaining a single counter 'z' that is updated
    according to a random hash function, and then the second moment is estimated
    as the square of this counter.
    """

    def __init__(self, n: int) -> None:
        """
        Initializes the AMS-F2-Estimate class.

        Parameters
        ----------
        n: int
            Size of the input universe.
        """
        self.n = n
        self.z = 0

        self.h_generator = HashGenerator(self.n, k=4, m=2)
        self.h = self.h_generator.generate_hash_function()

    def process_stream(self, stream: List[object]) -> None:
        """
        Executes the AMS-F2-Estimate algorithm on a stream (list) of elements.

        Parameters
        ----------
        stream: List[object]
            Stream of objects represented as a list.
        """
        for a_j in stream:
            self.z += (-1 if self.h_generator.hash_integer(a_j) == 0 else 1)

    def get_estimate(self) -> int:
        """
        Returns the estimated second moment of the stream.

        Returns
        -------
        int
            Estimated second moment of the stream.
        """
        return self.z ** 2