"""
This file contains tests for the swapping  module.
It tests if the functions correctly computes the output state of a noisy entanglement swapping.
"""

import math
from quantum_bell_api.utility import epr_pair
from quantum_bell_api import swapping

import unittest


def test_swap():
    # generate different Bell-diagonal pairs
    a_values = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 0.995, 0.999]
    pairs = [epr_pair(a, (1-a)/3, (1-a)/3, (1-a)/3) for a in a_values]

    # create the cartesian product pairs x pairs
    pairs_sq = [(pair1, pair2) for pair1 in pairs for pair2 in pairs]

    eta_p2_values = [1., 0.999, 0.995, 0.99]

    for pair1, pair2 in pairs_sq:
        for eta in eta_p2_values:
            new_pair = swapping.swap(pair1, pair2, eta=eta, p_2=eta)

            # check if the trace is preserved
            if not math.isclose(sum(new_pair), 1, rel_tol=1e-9):
                return False

            # check that the a value is lower or equal to the original pairs a value
            if new_pair.a > pair1.a or new_pair.a > pair2.a:
                return False

    return True


class TestSwap(unittest.TestCase):
    def test_swap(self):
        self.assertTrue(test_swap())


if __name__ == '__main__':
    unittest.main()
