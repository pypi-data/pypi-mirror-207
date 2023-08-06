from matplotlib import pyplot as plt
from sublinear.utils.hash_generator import HashGenerator

def test_hg_int():
    hg = HashGenerator(1000, 128, 10)
    hg.generate_hash_function()
    X = []
    for i in range(1000):
        X.append(hg.hash_integer(i))

    plt.hist(X)
    plt.show()