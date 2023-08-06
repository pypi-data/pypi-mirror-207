from typing import List
from math import ceil

class MisraGriesSketch:
    """
    The Misra-Gries sketch is a deterministic data structure
    that serves as a frequency table of events in a stream of data.
    
    It uses a dictionary to map events to frequencies and only uses
    sub-linear space, at the expense of undercounting some events due to
    frequency threshold.

    The Misra-Gries algorithm was invented in 1982 by Jayadev Misra and
    David Gries and described by them in a paper.
    """

    def __init__(self, epsilon: float):
        """
        Initializes Misra-Gries Sketch class.

        Parameters
        ----------
        epsilon: float
            Finds all items that occur more than ϵn times.

        """
        self.k = ceil(1 / epsilon)
        self.sketch = {}
        self.d = 0

    def process_stream(self, stream: List[object]) -> None:
        """
        Executes the Misra-Gries algorithm on a stream (list) of elements.

        Parameters
        ----------
        stream: List[object]
            Stream of objects represented as a list.

        """
        for value in stream:
            if value not in self.sketch:
                self.sketch[value] = 1
                self.d += 1
            else:
                self.sketch[value] += 1

            if self.d == self.k:
                for key in list(self.sketch.keys()):
                    self.sketch[key] -= 1
                    if self.sketch[key] == 0:
                        del self.sketch[key]
                self.d -= self.k

    def get_freq(self, values: List[object]) -> List[int]:
        """
        Returns the frequencies of elements in the Misra-Gries sketch.

        Parameters
        ----------
        values: List[object]
            List of elements for which to return frequencies.

        """
        frequencies = {}

        for value in values:
            if value in self.sketch:
                frequencies[value] = self.sketch[value]

        return frequencies