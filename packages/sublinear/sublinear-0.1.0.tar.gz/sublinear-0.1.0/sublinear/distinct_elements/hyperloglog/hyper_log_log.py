import hashlib
import math
from typing import List

from sublinear.utils.hash_generator import HashGenerator

class HyperLogLog:
    """
    HyperLogLog is a probabilistic algorithm for the count-distinct problem,
    approximating the number of distinct elements in a multiset with a
    trade-off between accuracy and memory usage.

    Attributes
    ----------
    b : int
        Number of bits for bucket address.
    m : int
        Number of buckets.
    alpha : float
        Correction factor.
    M : List[int]
        Bucket array to store maximum number of leading zeros.
    """

    def __init__(self, b: int):
        """
        Initializes HyperLogLog counter.

        Parameters
        ----------
        b : int
            Number of bits for bucket address.
        """
        self.b = b
        self.m = 2 ** self.b
        self.alpha = self._calculate_alpha()
        self.M = [0] * self.m

        self.h_generator = HashGenerator(128, 64, m=2**32)
        self.h = self.h_generator.generate_hash_function()

    def _calculate_alpha(self) -> float:
        """
        Calculate correction factor alpha based on the number of buckets (m).

        Returns
        -------
        float
            Correction factor alpha.
        """
        if self.m == 16:
            return 0.673
        if self.m == 32:
            return 0.697
        if self.m == 64:
            return 0.709
        if self.m >= 128:
            return 0.7213 / (1 + 1.079 / self.m)

    def _get_bucket_index(self, hash_value: int) -> int:
        """
        Extract the bucket index from the hash value.

        Parameters
        ----------
        hash_value : int
            Hash value of an item.

        Returns
        -------
        int
            Bucket index.
        """
        return hash_value & (self.m - 1)

    def _get_rho(self, hash_value: int) -> int:
        """
        Calculate the rank of the first 1-bit (rho) in the binary representation
        of the hash value.

        Parameters
        ----------
        hash_value : int
            Hash value of an item.

        Returns
        -------
        int
            Rank of the first 1-bit.
        """
        binary = format(hash_value, "032b")
        return binary[self.b:].find("1") + 1

    def add(self, item: str) -> None:
        """
        Add an item to the HyperLogLog counter.

        Parameters
        ----------
        item : str
            Input item to be added.
        """
        hash_value = self.h_generator.hash_string(item) 
        j = self._get_bucket_index(hash_value)
        w = hash_value >> self.b
        self.M[j] = max(self.M[j], self._get_rho(w))

    def estimate_cardinality(self) -> float:
        """
        Estimates the cardinality of the set.

        Returns
        -------
        float
            Estimated cardinality of the set.
        """
        Z = 1 / sum([2 ** -Mj for Mj in self.M])
        E = self.alpha * (self.m ** 2) * Z

        # No correction for intermediate range
        E_star = E

        # Apply small range correction
        if E <= 2.5 * self.m:
            V = self.M.count(0)
            if V != 0:
                E_star = self.m * math.log(self.m / V)
            else:
                E_star = E

        # Apply large range correction
        if E > (1 / 30) * (2 ** 32):
            E_star = (-2 ** 32) * math.log(1 - E / (2 ** 32))

        return E_star