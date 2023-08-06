# Experiment 1 (Test)

from collections import Counter
from ..count_min_sketch import CountMinSketch

def test_cms_1():

    epsilon = 0.01
    delta = 0.1
    cms = CountMinSketch(epsilon, delta)

    test1 = []

    for i in range(100):
        test1 += i * [f"word{i}"]

    cms.process_stream(test1)
    est_freq = cms.get_freq(test1)
    
    actual_freq = Counter(test1)
    
    error_freq = {}

    for word in actual_freq:
        diff = est_freq[word] - actual_freq[word]
        if diff not in error_freq:
            error_freq[diff] = 1
        else:
            error_freq[diff] += 1

    sorted_freqs = sorted(error_freq.items(), key=lambda x: x[0])
    N = sum(actual_freq.values())
    err = epsilon * N
    X, Y = list(zip(*sorted_freqs))
    acc = sum([pair[1] for pair in sorted_freqs if pair[0] < err])/sum(Y)

    avg_error = sum(X) / len(X)
    print(f"average error: {avg_error}")

    print(f"CMS Theory: error less than {err} with probability: {1 - delta}")
    print(f"actual error less than {err} with probability: {acc}")