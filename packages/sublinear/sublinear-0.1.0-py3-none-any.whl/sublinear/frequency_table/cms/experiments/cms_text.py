from math import ceil
import re
from matplotlib import pyplot as plt
from ..count_min_sketch import CountMinSketch

class CMS_Text():

    def __init__(self, epsilon: float, delta: float, path: str) -> None:
        """
        Initializes CMS Text class.

        Parameters
        ----------
        epsilon: float
            Epsilon from the epsilon-delta definition of the CMS.

        delta: float
            Delta from the epsilon-delta definition of the CMS.

        path: string
            Filepath to text file.

        """
        self.epsilon = epsilon
        self.delta = delta
        self.path = path

    def import_text(self, path: str):
        """
        Import text file from filepath.

        Parameters
        ----------
        path: string
            Filepath to text file.

        Returns
        -------
        corpus: list[str]
            List of strings containing cleaned input text.
        
        actual_freq: dict
            Dictionairy mapping frequencies to words in corpus.
            
        """
        with open(path, 'r') as file:
            raw = file.read().replace('\n', ' ')
            corpus = re.sub(r'[^A-Za-z0-9 ]+', '', raw).lower().split()

        actual_freq = {}

        for word in corpus:
            if word not in actual_freq:
                actual_freq[word] = 1
            else:
                actual_freq[word] += 1

        return corpus, actual_freq
    
    def compute_error(self, est_freq: dict, actual_freq: dict) -> dict:
        """
        Computes the absolute error between word frequency counts.

        Parameters
        ----------
        est_freq: dict
            Our estimated frequency from CMS.

        actual_freq: dict
            Actual frequency not seen by CMS.

        """
        error_freq = {}

        for word in actual_freq:
            diff = est_freq[word] - actual_freq[word]
            if diff not in error_freq:
                error_freq[diff] = 1
            else:
                error_freq[diff] += 1

        return error_freq
    
    def run(self):
        """
        Runs the CMS algorithm on the text input.

        """
        self.corpus, self.actual_freq = self.import_text(self.path)
        N = sum(self.actual_freq.values())

        print(f"Number of unique words: {len(self.actual_freq)}")
        print(f"Number of words, total: {N}")
        print()

        cms = CountMinSketch(self.epsilon, self.delta)

        print(f"width: {cms.K}")
        print(f"height: {cms.N}")

        print()

        # estimate less than epsilon * N with probability 1 - delta:

        self.err1 = 2 * N / cms.K
        self.err2 = self.epsilon * N

        print(f"Markov In.: error less than {self.err1} with probability: 0.5")
        print(f"CMS Theory: error less than {self.err2} with probability: {1 - self.delta}")
        print()

        cms.process_stream(self.corpus)
        cms.get_freq(self.corpus)

        est_freq = cms.frequencies
        self.est_freq = est_freq

    def plot_error(self):
        """
        Plots a graph that depicts the observed frequency
        of overestimating by a given amount.

        """
        error_freq = self.compute_error(self.est_freq, self.actual_freq)
        sorted_freqs = sorted(error_freq.items(), key=lambda x: x[0])

        X, Y = list(zip(*sorted_freqs))

        avg_error = sum(X) / len(X)
        print(f"average error: {avg_error}")
        print()

        acc1 = sum([pair[1] for pair in sorted_freqs if pair[0] < self.err1])/sum(Y)
        print(f"actual error less than {self.err1} with probability: {acc1}")

        acc2 = sum([pair[1] for pair in sorted_freqs if pair[0] < self.err2])/sum(Y)
        print(f"actual error less than {self.err2} with probability: {acc2}")

        plt.scatter(X, Y)
        plt.show()
