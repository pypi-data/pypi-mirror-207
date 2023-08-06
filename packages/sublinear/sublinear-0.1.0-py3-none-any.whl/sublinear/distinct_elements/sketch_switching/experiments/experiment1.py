from ...bjkst.bjkst_plus import BJKSTSketchPlus
from ..sketch_switch import SketchSwitch

def test_adv_robust_1():
    epsilon = 0.2
    delta = 0.1
    n = 128

    test1 = []

    for i in range(100):
        test1 += [f"word{i}"] # m = O(poly(n))

    insertion_only_de = SketchSwitch(BJKSTSketchPlus, epsilon, delta, len(test1), n)
    insertion_only_de.process_stream(test1)
    estimate = insertion_only_de.get_estimate()

    print("Estimated number of distinct elements:", estimate)