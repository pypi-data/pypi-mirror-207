import math
from typing import List
from sublinear.utils.hash_generator import HashGenerator
from sublinear.utils.zeros import Zeros

class BJKSTSketch:
    """
    The BJKST sketch is a probabilistic data structure
    that serves as a distinct element counter in a stream of data.

    It uses two hash functions and a set to estimate the number of distinct elements.
    It operates in sub-linear space, at the expense of some approximation error.

    The BJKST algorithm was invented by Bar-Yossef, Jayram, Kumar, Sivakumar, and Trevisan.
    """

    def __init__(self, n: int, epsilon: float, b: float = 10, max_input_length: int = 64, c: float = 576):
        """
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

        max_input_length: int, optional
            Maximum length of the input elements, used for generating hash functions.
        """
        self.n = n
        self.b = b
        self.c = c
        self.epsilon = epsilon

        self.z = 0
        self.B = set()

        self.h_generator = HashGenerator(self.n, max_input_length, m=n)
        self.h = self.h_generator.generate_hash_function()

        g_size = int(b * n * (epsilon ** (-4)) * (math.log(n) ** 2))
        self.g_generator = HashGenerator(self.n, max_input_length, m=g_size)
        self.g = self.g_generator.generate_hash_function()

    def process_stream(self, stream: List[object]) -> None:
        """
        Executes the BJKST algorithm on a stream (list) of elements.

        Parameters
        ----------
        stream: List[object]
            Stream of objects represented as a list.
        """
        for token in stream:
            h_j = self.h_generator.hash_string(token)
            zeros_hj = Zeros.zeros(h_j)
            if zeros_hj >= self.z:
                g_j = self.g_generator.hash_string(token) 
                self.B.add((g_j, zeros_hj))

                while len(self.B) >= self.c / (self.epsilon ** 2):
                    self.z += 1
                    self.B = {(a, b) for (a, b) in self.B if b >= self.z}

    def estimate_distinct_elements(self) -> int:
        """
        Returns the estimated number of distinct elements in the stream.

        Returns
        -------
        int
            Estimated number of distinct elements.
        """
        return len(self.B) * (2 ** self.z)