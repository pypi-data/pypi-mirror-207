import hashlib
from math import sqrt
import random
from typing import List

class HashGenerator():

    def __init__(self, n: int, k:int, m: int, p: int = None) -> None:
        """ 
        Initializes Hash class.

        Parameters
        ----------
        n: integer
            Input range.
            (e.g. for ASCII: n == 128)
        
        k: integer
            Input length. For strings, this would be the max
            input string length. Shorter strings are padded.

        m: integer
            Output dimension.
            ([n] -> [m])

        p: integer, optional
            Prime number such that p > n > m.

        """
        self.n = n
        self.k = k
        self.m = m
        self.p = p

        if not self.p:
            self.find_prime()

    def find_prime(self) -> None:
        """
        Starting from self.n, find the next larger prime number.

        """
        curr = max(self.n, self.m)
        
        while not self.p:
            upper = int(sqrt(curr))
            for i in range(2, upper + 1):
                if curr % i == 0:
                    break
                if i == upper:
                    self.p = curr
            
            curr += 1

    def generate_hash_function(self) -> List[int]:
        """
        Generates hash function as follows:
            select k integers {z1, ..., zk} by U.A.R. sampling 
            k times from the set {0, ..., p - 1}

        """
        self.z = [random.randint(0, self.p - 1) for i in range(self.k)]
        return self

    def hash_string(self, s: str) -> int:
        """
        Hashes input string as follows:
        h(a1, ..., ak) = (SUM_overall_zs zi * ai) mod p

        Parameters
        ----------
        s: string
            Input string to be hashed.

        """
        s = s.ljust(self.k, " ")
        emb = [ord(ch) for ch in s]

        z_a = sum(map(lambda x: x[0] * x[1], zip(self.z, emb[:self.k])))

        return  (z_a % self.p) % self.m

    def hash_integer(self, num: int) -> int:
        """
        Hashes an input integer as follows:
        h(x) = (SUM_overall_zs zi * x^i) mod p

        Parameters
        ----------
        num: int
            Input integer to be hashed.
        """
        z_a = sum(z_i * (num ** i) for i, z_i in enumerate(self.z))

        return (z_a % self.p) % self.m
    
    @staticmethod
    def hash_sha256(s: str, m: int) -> int:
        """
        Hashes the input string using the SHA-256 algorithm and maps the result to a specified range.

        Parameters
        ----------
        s: str
            Input string to be hashed.
        m: int
            The size of the output range, where the hash value will be mapped to an integer in [0, m).

        Returns
        -------
        int
            The hash value of the input string modulo m, an integer in the range [0, m).
        """
        s = s.encode()  # Convert the string to bytes
        hash_object = hashlib.sha256()
        hash_object.update(s)
        hash_value = int(hash_object.hexdigest(), 16)  # Convert the hex digest to an integer
        return hash_value % m