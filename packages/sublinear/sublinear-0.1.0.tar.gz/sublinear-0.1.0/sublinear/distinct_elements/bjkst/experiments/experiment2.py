# Experiment 1 (Test)

from ..bjkst_plus import BJKSTSketchPlus

def test_bjkst_plus():

    n = 128
    epsilon = 0.1
    delta = 0.1

    bjkst_plus = BJKSTSketchPlus(n, epsilon, delta)

    test1 = []

    for i in range(100):
        test1 += i * [f"word{i}"]

    bjkst_plus.process_stream(test1)

    estimate = bjkst_plus.estimate_distinct_elements()

    print("Estimated number of distinct elements:", estimate)