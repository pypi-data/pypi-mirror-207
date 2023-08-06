from typing import List, Type
from math import ceil, log

class SketchSwitch:
    """
    SketchSwitch is a robust streaming algorithm for estimating the number of
    distinct elements in a data stream. It improves the robustness of non-robust
    algorithms by maintaining multiple independent copies of the base algorithm
    and updating the estimate based on a specific condition.

    The base algorithm should provide (1 ± epsilon/20)-approximation
    with probability 1 - δ/(m^2).
    """

    def __init__(self, non_robust_algorithm: Type, epsilon: float, delta: float, m: int, n: int, *args, **kwargs):
        """
        Initializes the InsertionOnlyDE class.

        Parameters
        ----------
        non_robust_algorithm: Type
            The non-robust algorithm's class to be used as the base algorithm.

        epsilon: float
            The approximation error factor.

        delta: float
            The probability bound for the approximation.

        m: int
            Length of stream.

        n: int
            Size of the input universe.

        *args, **kwargs
            Additional arguments passed to the non-robust_algorithm's constructor.
        """
        self.epsilon = epsilon
        self.delta = delta
        self.m = m
        self.n = n
        self.t = ceil(epsilon**(-1) * log(m))

        self.algorithms = [non_robust_algorithm(n, epsilon / 20, delta / (m**2), *args, **kwargs) for _ in range(self.t)]
        self.estimate = 0
        self.index = 1

    def process_stream(self, stream: List[object]) -> None:
        """
        Processes the input stream using the base non-robust algorithms and
        updates the estimate according to the Insertion-only DE algorithm.

        Parameters
        ----------
        stream: List[object]
            The input stream of elements to be processed.
        """
        for item in stream:
            for algorithm in self.algorithms:
                algorithm.process_stream([item])

            if self.algorithms[self.index - 1].estimate_distinct_elements() >= (1 + self.epsilon / 2) * self.estimate:
                self.estimate = self.algorithms[self.index - 1].estimate_distinct_elements()
                self.index += 1

    def get_estimate(self) -> int:
        """
        Returns the current estimate of the number of distinct elements in the stream.

        Returns
        -------
        int
            The current estimate of the number of distinct elements.
        """
        return self.estimate
