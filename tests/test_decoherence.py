"""
This file contains tests for the decoherence module.
It tests if the functions correctly applies noise on a Bell-diagonal pair and preserves the trace.
"""

import math
from quantum_bell_api.utility import epr_pair
from quantum_bell_api import decoherence

import unittest


def test_depolarize():
    # generate different Bell-diagonal pairs
    a_values = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 0.995, 0.999]
    pairs = [epr_pair(a, (1-a)/3, (1-a)/3, (1-a)/3) for a in a_values]
    p_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for pair in pairs:
        for p in p_values:
            new_pair = decoherence.depolarize(pair, p)
            if not math.isclose(sum(new_pair), 1, rel_tol=1e-9):
                return False
    return True


class TestDecoherence(unittest.TestCase):
    def test_depolarize(self):
        self.assertTrue(test_depolarize())


if __name__ == '__main__':
    unittest.main()
